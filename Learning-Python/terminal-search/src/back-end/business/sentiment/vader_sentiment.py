from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def one_by_one_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)

    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        return "Positive", compound_score
    elif compound_score <= -0.05:
        return "Negative", compound_score
    else:
        return "Neutral", compound_score


class VaderSentiment:

    @staticmethod
    def process_title_sentiment(all_titles):
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(all_titles)

        compound_score = sentiment_scores['compound']

        if compound_score >= 0.05:
            return "Positive", compound_score
        elif compound_score <= -0.05:
            return "Negative", compound_score
        else:
            return "Neutral", compound_score

    @staticmethod
    def process_prompt_sentiment(prompt):
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(prompt)

        compound_score = sentiment_scores['compound']
        if compound_score >= 0.05:
            return "Positive"
        elif compound_score <= -0.05:
            return "Negative"
        else:
            return "Neutral"

    @staticmethod
    def process_prompt_one_by_one_sentiment(all_titles):
        all_ten_title = []
        for index, item in enumerate(all_titles, start=1):
            title_sentiment, score = one_by_one_sentiment(item['title'])
            all_ten_title.append({'title_index': index, 'vader_title': title_sentiment})
        return all_ten_title
