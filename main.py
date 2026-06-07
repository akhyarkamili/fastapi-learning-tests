from fastapi import APIRouter, FastAPI
import uvicorn


app = FastAPI(
    title="fastapi-learning-tests",
    version="0.1.0",
)

@app.get("/greetings")
def greetings() -> dict[str, str]:
    return {"message": "greetings"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8099)