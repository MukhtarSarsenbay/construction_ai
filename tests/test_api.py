from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_project():
    response = client.post("/api/v1/projects/", json={
        "project_name": "Test Project",
        "location": "Test Location"
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_project():
    response = client.get("/api/v1/projects/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1