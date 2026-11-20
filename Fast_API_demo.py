from fastapi import FastAPI
import requests

# Creamos la aplicación FastAPI
app = FastAPI()

# Endpoint que recibe solicitudes POST en /summarize
@app.post("/summarize")
def summarize(payload: dict):

# Mostramos en consola el JSON recibido
    print("\n--- Request recibido ---")
    print(payload)

# Enviamos el texto recibido a Ollama
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"Resume: {payload['text']}",
            "stream": False
        }
    )

    # Genera una excepción si Ollama devuelve un error HTTP
    response.raise_for_status()

    # Convertimos la respuesta a JSON
    result = response.json()

    # Mostramos la respuesta que recibimos del servicio externo
    print("--- Respuesta de Ollama ---")
    print(result["response"])

    # Devolvemos al cliente únicamente el resumen
    return {
        "summary": response.json()["response"]
    }

#comando 1 -> cd C:\Users\andre\Desktop\Python\Slalom_LL\Lunch_Learn_2_APIs\Sesion_1
#comando 2 -> python -m uvicorn Fast_API_demo:app --reload