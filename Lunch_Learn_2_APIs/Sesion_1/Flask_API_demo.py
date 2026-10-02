from flask import Flask, request
import requests

# Creamos la aplicación Flask
app = Flask(__name__)


# Endpoint que recibe solicitudes POST en /summarize
@app.route("/summarize", methods=["POST"])
def summarize():

    # Obtenemos el JSON enviado por el cliente
    data = request.json

    # Mostramos en consola lo que recibió nuestra API
    print("\n--- Request recibido ---")
    print(data)

    # Enviamos el texto recibido a Ollama
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"Resume: {data['text']}",
            "stream": False
        }
    )

    # Obtenemos la respuesta de Ollama
    result = response.json()

    # Mostramos la respuesta que recibimos del servicio externo
    print("--- Respuesta de Ollama ---")
    print(result)

    # Devolvemos al cliente únicamente el resumen
    return {
        "summary": result["response"]
    }


# Ejecutamos la aplicación
if __name__ == "__main__":
    app.run(debug=True)