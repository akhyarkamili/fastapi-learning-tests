from fastapi import APIRouter

from routers.greetings import hello

router = APIRouter(tags=["convo-starter"])
router.add_api_route("/hello", hello, methods=["GET"])

@router.get("/good-morning")
def good_morning() -> dict[str, str]:
    return {"message": "good morning"}
