from fastapi import APIRouter, FastAPI

from routers.convo_starter import router as convo_starter_router
from routers.greetings import v1

app = FastAPI(
    title="fastapi-learning-tests",
    version="0.1.0",
)

# app.include_router(greetings_router, prefix="/greetings")

app.include_router(v1)
# app.include_router(convo_starter_router, prefix="/convo-starter")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, FastAPI!"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
