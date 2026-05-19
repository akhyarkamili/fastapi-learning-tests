# fastapi-learning-tests

FastAPI starter managed with [uv](https://docs.astral.sh/uv/).

## Setup

Dependencies are already installed in `.venv`. To sync again:

```bash
uv sync
```

## Run

Development server with auto-reload:

```bash
uv run uvicorn main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) for the API and [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive docs.

## Endpoints

| Path          | Description        |
|---------------|--------------------|
| `GET /`       | Hello message      |
| `GET /health` | Health check       |
| `GET /hello`  | Greeting (router)  |
| `GET /hi`     | Greeting (router)  |
