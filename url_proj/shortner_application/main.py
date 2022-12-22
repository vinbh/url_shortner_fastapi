from fastapi import FastAPI, HTTPException
import validators
import schemas


app = FastAPI()


def raise_bad_req(message):
    raise HTTPException(status_code=400, detail=message)

@app.get("/")
def read_root():
    return "Hello test"


@app.post("/url")
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_req(message="your provided URL isnt valid")
    return f"todo: make db netry {url.target_url}"    


