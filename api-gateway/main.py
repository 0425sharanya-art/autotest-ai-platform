from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def health():
    return {"message": "AutoTestAI Gateway Running"}

@app.post("/run-tests")
def run_tests():
    response = requests.post("http://test-runner:8001/run")
    return response.json()
