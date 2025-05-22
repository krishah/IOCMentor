import requests
from config import OLLAMA_SERVER, LLM_MODEL, LLM_PROMPT

def ask_llm(ioc, results):
    merged = "\n".join(f"{k}: {v}" for k, v in results.items())
    prompt = LLM_PROMPT.format(ioc=ioc, results=merged)
    response = requests.post(f"{OLLAMA_SERVER}/api/generate", json={
        "model": LLM_MODEL,
        "prompt": prompt,
        "stream": False
    })
    if response.ok:
        return response.json().get("response", "Brak odpowiedzi od LLM.")
    return "Błąd zapytania do LLM."
