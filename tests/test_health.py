from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_request():

    response = client.get("/health")

    #Assertions
    assert response.status_code == 200
    assert response.json() == {"message": "Successful Health Check!"}

