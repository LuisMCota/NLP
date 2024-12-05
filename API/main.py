from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os
from typing import List

# Cargar el modelo guardado usando pickle
with open("tfidf_logistic_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

# Crear la instancia de FastAPI
app = FastAPI()

class Reviews(BaseModel):
    texts: List[str]  # Asegúrate de que sea una lista de textos

@app.post("/predict")
def predict_polarity(reviews: Reviews):
    results = []
    
    for text in reviews.texts:  # Iterar sobre la lista de textos
        prediction = model.predict([text])[0]
        polarity = "positive" if prediction == 2 else "negative"
        results.append({"text": text, "polarity": polarity})
    
    return {"predictions": results}

# Obtener el puerto desde la variable de entorno o usar 8080 por defecto
port = int(os.getenv("PORT", 8080))

if __name__ == "__main__":
    import uvicorn
    # Iniciar la aplicación FastAPI en el puerto especificado
    uvicorn.run(app, host="0.0.0.0", port=port)
