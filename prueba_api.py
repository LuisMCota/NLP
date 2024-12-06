import requests
import json

# Define URLs for both endpoints
predict_url = "https://my-api-826110093544.us-central1.run.app/predict"
convert_to_negative_url = "https://my-api-826110093544.us-central1.run.app/convert_to_negative"

# Load the data from the text.json file (this file should contain a list of texts)
with open('text.json', 'r') as f:
    data = json.load(f)

# Function to test the /predict endpoint
def test_predict_endpoint(data):
    response = requests.post(predict_url, json=data)
    if response.status_code == 200:
        print("Polarity Predictions:")
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# Function to test the /convert_to_negative endpoint
def test_convert_to_negative_endpoint(data):
    response = requests.post(convert_to_negative_url, json=data)
    if response.status_code == 200:
        print("Converted Texts (Positive to Negative):")
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# Call both endpoints
test_predict_endpoint(data)
test_convert_to_negative_endpoint(data)
