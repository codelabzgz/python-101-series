from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def getSentiment(text):
    if len(text) > 512:
        text = text[:512]

    sentiments = sentiment_pipeline([text])
    return sentiments