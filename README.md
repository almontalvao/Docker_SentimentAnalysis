# Step by Step: Containerizing a Sentiment Analyzer

This repo shows in details how to use the containerized sentiment analyser developed for this project. The process was developed using Ubuntu on WSL2 through Windows Terminal. FastAPI was used to deploy the model and Docker was used to create the container.

## Create a folder and set it as your directory

```python
mkdir my_container && cd $_
```

## Clone this repo 

```python
 git clone https://github.com/almontalvao/Docker_SentimentAnalysis.git
```

## Docker image and container

```python
docker build -t fastapi-demo .
docker run -dp 8000:8000 fastapi-demo
```

## Access the API

To access the API:

```python
POST http://{IP_ADDRESS}/predict_sentiment
```

For example, replace the string as below:

```python
{"query_string": "excited"}
```
