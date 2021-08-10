from django.test import TestCase
from .sentiment_analyzer import get_article_sentiment


class SentimentTest(TestCase):

    pos_text = """
    This is a positive text. What a great story. Excellent!
    I feel so much joy. This is fantastic! Awesome!
    I love Hungary!
    """
    neg_text = """
    This is a negative text. What a terrible story. Horrible!
    I feel so sad. This is depressing! Awful!
    I don't like China!
    """

    def test_score(self):
        pos_score = int(get_article_sentiment(self.pos_text))
        neg_score = int(get_article_sentiment(self.neg_text))
        self.assertEqual(pos_score > 0, True) 
        self.assertEqual(neg_score < 0, True)

