import requests
import json

# Cuando instalamos y ejecutamos Ollama, este inicia un servicio local que expone una API HTTP. 
# Por defecto se configura en: http://localhost:11434

OLLAMA_URL = "http://localhost:11434/api/generate" # En este caso, este es el endpoint

payload = {
    "model": "llama3",
    "prompt": "Tell me about Checo Perez",
    "stream": False
}

response = requests.post(
    OLLAMA_URL,
    json=payload
)

response.raise_for_status()

data = response.json()

print("=== RESPUESTA DEL MODELO ===")
print(data["response"])

print("=== JSON COMPLETO RECIBIDO ===")
print(
    json.dumps(
        response.json(),
        indent=4,
        ensure_ascii=False
    )
)