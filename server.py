from fastapi import FastAPI
from pipeline import run_pipeline

app = FastAPI()

@app.post("/generate")
def generate(data: dict):
    result = run_pipeline(data)

    return result