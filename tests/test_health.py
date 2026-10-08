#Going to import FastAPI TestClient and app object from app.main
# Test function
# GET request /health
# assert: code is 200, response message contains correct status
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_request():

    response = client.get("/health")

    #Assertions
    assert response.status_code == 200
    assert response.json() == {"message": "Successful Health Check!"}

