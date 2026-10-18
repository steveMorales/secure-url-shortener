from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_diff_urls_get_diff_codes():
    response = client.post("/shorten", json={"url": "https://youtube.com"})
    response2 = client.post("/shorten", json={"url": "https://www.wikipedia.org/"})

    data = response.json()
    data2 = response2.json()

    #Assertions
    assert response.status_code == 201
    assert response2.status_code == 201
    assert data["code"] != data2["code"]

def test_both_codes_redirect_to_their_own_urls():
    code1 = client.post("/shorten", json={"url": "https://youtube.com"}).json()["code"]
    code2 = client.post("/shorten", json={"url": "https://www.wikipedia.org/"}).json()["code"]

    r1 = client.get(f"/{code1}", follow_redirects=False)
    r2 = client.get(f"/{code2}", follow_redirects=False)

    assert r1.headers["location"].rstrip("/") == "https://youtube.com"
    assert r2.headers["location"].rstrip("/") == "https://www.wikipedia.org"
