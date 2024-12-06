from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os
from typing import List
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Load the logistic regression model for polarity prediction using pickle
with open("tfidf_logistic_regression_model.pkl", "rb") as file:
    polarity_model = pickle.load(file)

# Load the T5 tokenizer and model for text transformation (positive to negative)
tokenizer = T5Tokenizer.from_pretrained('./', config='./tokenizer_config.json')
model = T5ForConditionalGeneration.from_pretrained('./', config='./tokenizer_config.json')

# Check if GPU is available and move the model to the appropriate device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# Create FastAPI instance
app = FastAPI()

# Define the data model for the input
class Reviews(BaseModel):
    texts: List[str]  # A list of texts for prediction and transformation

# Endpoint for polarity prediction
@app.post("/predict")
def predict_polarity(reviews: Reviews):
    results = []
    
    for text in reviews.texts:  # Iterate over the list of texts
        prediction = polarity_model.predict([text])[0]  # Predict polarity using the logistic regression model
        polarity = "positive" if prediction == 2 else "negative"
        results.append({"text": text, "polarity": polarity})
    
    return {"predictions": results}

# Endpoint for converting text to negative (positive to negative transformation)
@app.post("/convert_to_negative")
async def convert_to_negative(reviews: Reviews):
    results = []
    
    for text in reviews.texts:  # Iterate over the list of texts
        # Tokenize the input text
        inputs = tokenizer(f"Convert to negative: {text}", return_tensors="pt").to(device)
        
        # Generate the output
        output_ids = model.generate(inputs["input_ids"])
        
        # Decode the output tokens to readable text
        output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        
        results.append({"original_text": text, "converted_text": output_text})
    
    return {"converted_texts": results}

# Get the port from environment variable or use default 8080
port = int(os.getenv("PORT", 8080))

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
