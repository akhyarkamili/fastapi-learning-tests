from fastapi import APIRouter

router = APIRouter(prefix="/greetings", tags=["greetings"])

@router.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "hello"}


@router.get("/hi")
def hi() -> dict[str, str]:
    return {"message": "hi"}

v1 = APIRouter(prefix="/v1")
v1.include_router(router)