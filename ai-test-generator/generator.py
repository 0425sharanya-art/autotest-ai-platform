import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_test(api_description):

    prompt = f"""
Generate a pytest test case for this API.

API:
{api_description}

Use requests library.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model":"llama3",
            "prompt":prompt,
            "stream":False
        }
    )

    return response.json()["response"]
