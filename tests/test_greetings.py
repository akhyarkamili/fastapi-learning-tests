from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_hello_returns_200() -> None:
    response = client.get("/greetings/hello")
    assert response.status_code == 404


def test_v1_returns_200() -> None:
    response = client.get("/v1/greetings/hello")
    assert response.status_code == 200
