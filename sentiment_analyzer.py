import nltk
from statistics import mean
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def get_article_sentiment(article_text: str) -> float:
    tokenized_sentences = nltk.sent_tokenize(article_text)
    scores = [sia.polarity_scores(sentences)["compound"] for sentences in tokenized_sentences]
    return mean(scores)*100
