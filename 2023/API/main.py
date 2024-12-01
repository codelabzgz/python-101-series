from scrapper_svc import getArticle
from transformers_svc import getSentiment
from datetime import datetime
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def setStatus(): 
    now = datetime.utcnow()
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    return {
        "status": {
            "timestamp": timestamp,
            "error_code": 0,
            "error_message": "Successful",
            "env": getenv("ENV")
        }
    }


app = FastAPI()

@app.get("/")
def read_root():
    return setStatus()


@app.post("/")
def read_item(url: str):
    summary = getArticle(url)
    sentiment = getSentiment(summary)

    res = setStatus()
    res["data"] = {
        "summary": summary,
        "sentiment": sentiment
    }
    return res

    