from textblob import TextBlob


class TextBlobSentiment:

    @staticmethod
    def process_title_sentiment(all_titles):
        blob = TextBlob(all_titles)
        sentiment_score = blob.sentiment.polarity

        if sentiment_score > 0:
            return "Positive", sentiment_score
        elif sentiment_score < 0:
            return "Negative", sentiment_score
        else:
            return "Neutral", sentiment_score

    @staticmethod
    def process_prompt_sentiment(prompt):
        sentiment_analysis = TextBlob(prompt)
        sentiment_score = sentiment_analysis.sentiment.polarity

        if sentiment_score > 0:
            return "Positive"
        elif sentiment_score < 0:
            return "Negative"
        else:
            return "Neutral"
