from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_shorten_returns_201_and_code():
    response = client.post("/shorten", json={"url": "https://youtube.com"})

    #store data in-memory dict
    data = response.json()

    #Assertions
    assert response.status_code == 201
    assert isinstance(data["code"], str)
    assert len(data["code"]) > 0

def test_shorten_rejects_missing_url():
    response = client.post("/shorten", json={})

    assert response.status_code == 422
    


