import requests
import json

# URL de la API desplegada en Google Cloud Run
url = "https://my-api-826110093544.us-central1.run.app/predict"

# Cargar los datos desde el archivo text.json
with open('text.json', 'r') as f:
    data = json.load(f)

# Realizar la solicitud POST a la API
response = requests.post(url, json=data)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Imprimir la respuesta de la API
    print("Predictions:")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)