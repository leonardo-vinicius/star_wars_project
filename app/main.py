# app/main.py
from fastapi import FastAPI

app = FastAPI(
    title="Star Wars API",
    description="API para consumo de dados do universo Star Wars",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
