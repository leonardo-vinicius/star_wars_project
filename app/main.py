from fastapi import FastAPI
from functions_framework import http
from fastapi.middleware.wsgi import WSGIMiddleware

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@http
def starwars_api(request):
    return WSGIMiddleware(app)(request)
