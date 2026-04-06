from fastapi import FastAPI
from generator import generate_test

app = FastAPI()

@app.post("/generate-test")
def generate(api: str):

    test_code = generate_test(api)

    return {"generated_test": test_code}
