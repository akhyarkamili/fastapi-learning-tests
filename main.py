from fastapi import FastAPI

from routers.greetings import router as greetings_router

app = FastAPI(
    title="fastapi-learning-tests",
    version="0.1.0",
)

app.include_router(greetings_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, FastAPI!"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
