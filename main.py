from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class PredictionRequest(BaseModel):
  query_string: str

@app.get("/health")
def health():
    return "Service is online."

@app.post("my-endpoint")
def my_endpoint(request: PredictionRequest):
    sentiment_model = pipeline("sentiment-analysis")
    sentiment_query_sentence = get_random_comment(top_comments)
    sentiment = sentiment_model(sentiment_query_sentence)
    return print(f"Sentiment test: {sentiment_query_sentence} == {sentiment}")