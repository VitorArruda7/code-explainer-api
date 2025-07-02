from fastapi.testclient import TestClient
from app.main import app
from app.services.mock_openai_service import MockOpenAIService
from app.routes import code_routes

client = TestClient(app)
app.dependency_overrides[code_routes.get_openai_service] = MockOpenAIService

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_explain_code_mock():
    payload = {
        "code_snippet": "print('Hello, world!')",
        "language": "python"
    }
    response = client.post("/explain", json=payload)
    assert response.status_code == 200
    assert "Mock explanation" in response.json()["explanation"]