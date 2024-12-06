# FastAPI Application: Sentiment Analysis and Text Transformation

This FastAPI application provides two main features:
1. **Polarity Prediction**: Predicts whether a given text has a positive or negative sentiment using a pre-trained logistic regression model.
2. **Text Transformation**: Converts positive texts into negative ones using a pre-trained T5 model.

### API URL
You can access the API at: [https://my-api-826110093544.us-central1.run.app](https://my-api-826110093544.us-central1.run.app)

## Key Imports
- **FastAPI**: Web framework for building the API.
- **pydantic.BaseModel**: For defining the input data model.
- **pickle**: Used to load the pre-trained logistic regression model.
- **os**: For managing environment variables and file paths.
- **List**: From `typing`, used to define the list of texts for input validation.
- **transformers.T5Tokenizer** and **T5ForConditionalGeneration**: Used to load the T5 model for text transformation.
- **torch**: For checking GPU availability and running the model.

## Models

### 1. Loading Models
- **Polarity Model**: A logistic regression model is loaded via `pickle` to predict whether the sentiment of a text is positive or negative.
- **T5 Model**: A T5 model and tokenizer are used for transforming text from positive to negative. The model is loaded locally from the specified files.

### 2. FastAPI Instance
An instance of **FastAPI** is created to handle incoming HTTP requests.

### 3. Data Models
The `Reviews` class, based on `BaseModel`, is used to validate the incoming request data. It expects a list of strings (`texts`), which are the reviews or sentences to be processed.

## Endpoints

### `/predict` - Polarity Prediction
- **Method**: `POST`
- **Input**: A JSON object containing a list of texts (`texts`).
- **Output**: A JSON object with the sentiment polarity of each text (`positive` or `negative`).

### Endpoint: `/convert_to_negative`

This endpoint is designed to convert positive texts into negative ones using a pre-trained T5 model. The functionality utilizes the T5 model for **conditional text generation**, specifically generating a negative form of the input text.

#### Method:
- **POST**: The client sends a POST request with a JSON body that includes a list of texts. The server then processes these texts and returns the transformed negative versions.

#### Input:
- The input to this endpoint is a JSON object with a key `texts`, which contains a list of strings (reviews or sentences). These texts will be transformed into their negative counterparts.

**Example Request**:
```json
{
  "texts": ["I love this product!", "This is a terrible product."]
}
