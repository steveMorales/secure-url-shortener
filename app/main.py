from fastapi import FastAPI, status, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
from app.utils import random_code_generation

class UrlResponse(BaseModel):
    code : str

class UrlRequest(BaseModel):
    url : HttpUrl

app = FastAPI()

url_store = {} #maps code -> original URL

@app.get("/health")
def get_health():
    return {"message": "Successful Health Check!"}

@app.post("/shorten", response_model=UrlResponse, status_code=status.HTTP_201_CREATED)
def post_shorten(payload : UrlRequest):
    code = random_code_generation()
    #loop until code is not in url store to avoid collisions
    while code in url_store:
        code = random_code_generation()
    url_store[code] = str(payload.url)

    return {"code" : code}

@app.get("/{code}")
def get_redirect(code : str):
    original_url = url_store.get(code)

    if original_url is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Code not found")

    return RedirectResponse(url=original_url, status_code=status.HTTP_302_FOUND)

