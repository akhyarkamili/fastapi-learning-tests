from fastapi.testclient import TestClient

from fastapi import APIRouter, Depends, FastAPI, Request, Query

def test_router_includes():
    router = APIRouter(prefix="/greetings", tags=["greetings"])
    convo_starter = APIRouter(prefix="/convo-starter", tags=["convo-starter"])

    @convo_starter.get("/hello")
    @router.get("/hello")
    def hello() -> dict[str, str]:
        return {"message": "hello"}

    @router.get("/hi")
    def hi() -> dict[str, str]:
        return {"message": "hi"}

    v1 = APIRouter(prefix="/v1")
    v1.include_router(router)
    v1.include_router(router, prefix="/yet-another-prefix")
    v1.include_router(convo_starter)

    app = FastAPI(
        title="fastapi-learning-tests",
        version="0.1.0",
    )
    app.include_router(v1)
    client = TestClient(app)

    response = client.get("/greetings/hello")
    assert response.status_code == 404, "hello should not be directly available"

    response = client.get("/v1/greetings/hello")
    assert response.status_code == 200, "hello should be mounted under v1/greetings"

    response = client.get("/v1/convo-starter/hello")
    assert response.status_code == 200, "hello should be mounted under convo-starter with double decorator"

    response = client.get("/v1/yet-another-prefix/greetings/hello")
    assert response.status_code == 200, "/greetings/hello should be mounted under yet-another-prefix"


def test_dependency_injection():
    def get_name() -> str:
        return "John"

    app = FastAPI(
        title="fastapi-learning-tests",
        version="0.1.0",
    )

    @app.get("/hello")
    def hello(request: Request, name: str = Depends(get_name), age: int | None = Query(default=None)) -> dict[str, str]:
        route = request.scope.get("route")
        path = route.path if route else "unknown"
        return {"message": f"hello {name}, {age}, you called endpoint {path}"}

    client = TestClient(app)

    response = client.get("/hello")
    assert response.json() == {"message": "hello John, None, you called endpoint /hello"}

    response = client.get("/hello?age=20")
    assert response.json() == {"message": "hello John, 20, you called endpoint /hello"}

def test_trailing_slash():
    app = FastAPI(
        title="fastapi-learning-tests",
        version="0.1.0",
    )

    @app.get("/hello/")
    def hello(request: Request) -> dict[str, str]:
        route = request.scope.get("route")
        path = route.path if route else "unknown"
        return {"message": f"hello, you called endpoint {path}"}

    client = TestClient(app)

    response = client.get("/hello")
    assert response.json() == {"message": "hello, you called endpoint /hello/"}

    response = client.get("/hello/")
    assert response.json() == {"message": "hello, you called endpoint /hello/"}

def test_no_trailing_slash_():
    app = FastAPI(
        title="fastapi-learning-tests",
        version="0.1.0",
    )

    @app.get("/hello")
    def hello(request: Request) -> dict[str, str]:
        route = request.scope.get("route")
        path = route.path if route else "unknown"
        return {"message": f"hello, you called endpoint {path}"}

    client = TestClient(app)

    response = client.get("/hello")
    assert response.json() == {"message": "hello, you called endpoint /hello"}

    response = client.get("/hello/")
    assert response.status_code == 200, "should succeed with trailing slash"
    assert response.json() == {"message": "hello, you called endpoint /hello"}


    response = client.get("/hello/", follow_redirects=False)
    assert response.status_code == 307, "should redirect to /hello"
    assert response.headers.get("Location") == str(client.base_url) + "/hello", "should redirect to /hello"


def test_trailing_slash_router():
    app = FastAPI(
        title="fastapi-learning-tests",
        version="0.1.0",
    )

    router = APIRouter(prefix="/hello")
    @router.get("")
    def hello(request: Request) -> dict[str, str]:
        route = request.scope.get("route")
        path = route.path if route else "unknown"
        return {"message": f"hello, you called endpoint {path}"}
    app.include_router(router)
    
    client = TestClient(app)

    response = client.get("/hello")
    assert response.status_code == 200 

    response = client.get("/hello/")
    assert response.status_code == 200, "should succeed with trailing slash"
    assert response.json() == {"message": "hello, you called endpoint /hello"}

    response = client.get("/hello/", follow_redirects=False)
    assert response.status_code == 307, "should redirect to /hello"
    assert response.headers.get("Location") == str(client.base_url) + "/hello", "should redirect to /hello"

def test_header():
    def get_name() -> str:
        return "John"

    app = FastAPI(
        title="fastapi-learning-tests",
        version="0.1.0",
    )

    @app.get("/hello")
    def hello(request: Request, name: str = Depends(get_name), age: int | None = Query(default=None)) -> dict[str, str]:
        header : str = request.headers.get('X-Header')
        return {"message": f"hello {name}, {age}, you passed header {header}"}

    client = TestClient(app, raise_server_exceptions=False)

    client.headers.update({"X-Header": "1"})
    response = client.get("/hello")
    assert response.json() == {"message": "hello John, None, you passed header 1"}, "should succeed with str"

    client.headers.update({"X-Header": 1}) # crashes
    # response = client.get("/hello")
    # assert response.status_code == 500, "should fail with int"