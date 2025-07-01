from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_explain_code():
    payload = {
        "code_snippet": "print('Hello World')",
        "language": "Python"
    }
    response = client.post("/explain", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "Explicação mock" in data["explanation"]
    assert "Sugestões de melhoria mock" in data["improvements"]