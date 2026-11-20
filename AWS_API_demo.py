
import requests

API_URL = "https://56cb5yls7t2czphqvvsbpzx2oa0djngo.lambda-url.us-east-1.on.aws"

# 1. Comprobar que la API está disponible
response = requests.get(f"{API_URL}/health", timeout=30)

print("Health:", response.status_code, response.json())

# 2. Consultar los archivos existentes en S3
response = requests.get(f"{API_URL}/files", timeout=30)

print("Archivos existentes:", response.status_code)
print(response.json())

# 3. Enviar contenido a AWS para guardarlo en S3
payload = {
    "file_name": "sales_demo.csv",
    "content": "id,amount\n1,100\n2,200\n"
}

response = requests.post(
    f"{API_URL}/files",
    json=payload,
    timeout=30
)

print("Carga:", response.status_code)
print(response.json())

# 4. Consultar nuevamente los archivos
response = requests.get(f"{API_URL}/files", timeout=30)

print("Archivos después de la carga:", response.json())
