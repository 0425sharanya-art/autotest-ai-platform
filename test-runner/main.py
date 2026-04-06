from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.post("/run")
def run_tests():

    result = subprocess.run(
        ["pytest", "../api-tests"],
        capture_output=True,
        text=True
    )

    return {
        "output": result.stdout,
        "errors": result.stderr
    }
