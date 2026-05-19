from fastapi import APIRouter

router = APIRouter(tags=["greetings"])


@router.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "hello"}


@router.get("/hi")
def hi() -> dict[str, str]:
    return {"message": "hi"}
