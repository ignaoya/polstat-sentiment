import nltk
import requests
from statistics import mean
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
API_URL = 'http://localhost:8000/api/articles/'


def get_article_sentiment(article_text: str) -> int:
    tokenized_sentences = nltk.sent_tokenize(article_text)
    scores = [sia.polarity_scores(sentences)["compound"] for sentences in tokenized_sentences]
    return int(mean(scores)*100)

def rate_unrated_articles():
    res = requests.get(API_URL)
    for article in res.json():
        if article['rating'] == 0:
            article['rating'] = get_article_sentiment(article['text'])
            art_id = str(article.pop('id'))
            requests.put(API_URL + art_id + '/', data=article)


if __name__ == '__main__':
    rate_unrated_articles()

