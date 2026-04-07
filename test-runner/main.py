from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def health():
    return {"status": "Test Runner Service Running"}

@app.post("/run")
def run_tests():

    result = subprocess.run(
        ["pytest"],
        capture_output=True,
        text=True
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "return_code": result.returncode
    }
