# Polarity Prediction and Text Transformation API

This API is designed to perform two text-related tasks:

1. **Polarity Prediction**: Classifies texts as "positive" or "negative" using a trained logistic regression model.
2. **Text Transformation (Positive to Negative)**: Converts positive texts into their negative counterparts using a T5-based model.

The API is hosted and available at the following URL:

**API URL**: [https://my-api-826110093544.us-central1.run.app](https://my-api-826110093544.us-central1.run.app)

## Endpoints

### 1. `/predict` - Polarity Prediction

This endpoint receives a list of texts and returns the polarity of each (positive or negative) using a logistic regression model.

#### Method: `POST`

#### Request Body:
```json
{
  "texts": [
    "I love this product",
    "This service is terrible"
  ]
}
