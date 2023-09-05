from textblob import TextBlob


def one_by_one_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        return "Positive", sentiment_score
    elif sentiment_score < 0:
        return "Negative", sentiment_score
    else:
        return "Neutral", sentiment_score


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

    @staticmethod
    def process_prompt_one_by_one_sentiment(all_titles):
        all_ten_title = []
        for index, item in enumerate(all_titles, start=1):
            title_sentiment, score = one_by_one_sentiment(item['title'])
            all_ten_title.append({'title_index': index, 'blob_title': title_sentiment})
        return all_ten_title
