from fastapi import FastAPI
from analyzer import analyze_log

app = FastAPI()

@app.get("/")
def health():
    return {"message": "Defect Analyzer Service Running"}

@app.post("/analyze")
def analyze(log: str):
    result = analyze_log(log)
    return {
        "analysis": result
    }
