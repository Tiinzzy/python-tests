import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")


def one_by_one_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)

    if sentiment_scores['compound'] >= 0.05:
        return "Positive", sentiment_scores
    elif sentiment_scores['compound'] <= -0.05:
        return "Negative", sentiment_scores
    else:
        return "Neutral", sentiment_scores


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

    @staticmethod
    def process_prompt_one_by_one_sentiment(all_titles):
        all_ten_title = []
        for index, item in enumerate(all_titles, start=1):
            title_sentiment, score = one_by_one_sentiment(item['title'])
            all_ten_title.append({'title_index': index, 'nltk_title': title_sentiment, 'title': item['title']})
        return all_ten_title
