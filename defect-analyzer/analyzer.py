import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_log(log):

    prompt = f"""
Analyze this test failure log.

Log:
{log}

Classify root cause:

1 UI locator issue
2 API failure
3 Backend bug
4 Network issue

Return category only.
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
