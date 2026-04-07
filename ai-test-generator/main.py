from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.get("/")
def health():
    return {"status": "AI Test Generator Running"}

@app.post("/generate-test")
def generate_test(api_description: str):

    prompt = f"""
Generate a pytest API test for this API.

API Description:
{api_description}

Use Python requests library.
Return only the pytest code.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return {
        "generated_test": response.json()["response"]
    }
