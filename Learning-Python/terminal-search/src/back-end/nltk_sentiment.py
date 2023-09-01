import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")


class NLTKSentiment:

    @staticmethod
    def process_title_sentiment(all_titles):
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(all_titles)

        if sentiment_scores['compound'] >= 0.05:
            return "Positive", sentiment_scores
        elif sentiment_scores['compound'] <= -0.05:
            return "Negative", sentiment_scores
        else:
            return "Neutral", sentiment_scores

    @staticmethod
    def process_prompt_sentiment(prompt):
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(prompt)

        if sentiment_scores['compound'] >= 0.05:
            return "Positive"
        elif sentiment_scores['compound'] <= -0.05:
            return "Negative"
        else:
            return "Neutral"
