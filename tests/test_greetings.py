from fastapi.testclient import TestClient

from fastapi import APIRouter, FastAPI 

def test_router_includes() -> None:
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
