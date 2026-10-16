from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_redirect_returns_302_to_orig_url():
    post_response = client.post("/shorten", json={"url": "https://youtube.com"})
    code = post_response.json()["code"]

    #Request code without redirect
    response = client.get(f"/{code}", follow_redirects=False)

    assert response.status_code == 302
    assert response.headers["location"].rstrip("/") == "https://youtube.com"

def test_unknown_code_returns_404():
    response = client.get("/doesnotexist", follow_redirects=False)

    assert response.status_code == 404