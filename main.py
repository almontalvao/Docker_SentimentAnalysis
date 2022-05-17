from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

app = FastAPI()

sentiment_model = pipeline("sentiment-analysis")

def sentiment_prediction(sentiment_query_sentence):
  sentiment = sentiment_model(sentiment_query_sentence)
  print(f"Sentiment test: {sentiment_query_sentence} == {sentiment}")
  return sentiment

class PredictionRequest(BaseModel):
  query_string: str

@app.get("/health")
def health():
    return "Service is online."

@app.post("/predict_sentiment")
def my_endpoint(request: PredictionRequest):
  return sentiment_prediction(request.query_string)
 
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')