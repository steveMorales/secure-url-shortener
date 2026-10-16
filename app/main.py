from fastapi import FastAPI, status
from pydantic import BaseModel, HttpUrl

class UrlResponse(BaseModel):
    code : str

class UrlRequest(BaseModel):
    url : HttpUrl

app = FastAPI()

@app.get("/health")
def get_health():
    return {"message": "Successful Health Check!"}

@app.post("/shorten", response_model=UrlResponse, status_code=status.HTTP_201_CREATED)
def post_shorten(payload : UrlRequest):
    code = "50test"
    return {"code" : code}


