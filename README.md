# Step by Step: Containerizing a Sentiment Analyzer

This repo shows in details how I built and and containerized a sentiment analyzer.

## Prerequisites
The process was developed using Ubuntu on WSL2 through Windows Terminal. FastAPI was used to deploy the model and Docker was used to create the container.

### Part 1
Create a new GitHub repository, virtual environment, and local server.

In Ubuntu,create and activate a new virtual environment:

conda create -n fastapi_env python=3.8 pip

conda activate fastapi_env

Install required packages:

pip install fastapi uvicorn

pip freeze > requirements.txt

Then add a "main" python file where the code will be stored:

touch main.py

In your prefered IDE write a health check endpoint:

from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return "Service is online."

Then it's time to launch your server locally, using the terminal screen of your IDE: 

uvicorn main:app --port 8000

Make sure the process ran smoothly by checking the local host: http://127.0.0.1:8000. 

Commit these changes and push them to the repo you created for the project.

### Part 2
