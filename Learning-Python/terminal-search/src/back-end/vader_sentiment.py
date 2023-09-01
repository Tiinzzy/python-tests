from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class VaderSentiment:

    @staticmethod
    def process_title_sentiment(all_titles):
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(all_titles)
        print(sentiment_scores, 'regular?')

        compound_score = sentiment_scores['compound']
        print(compound_score, 'compound')

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
        print(compound_score, 'search')
        if compound_score >= 0.05:
            return "Positive"
        elif compound_score <= -0.05:
            return "Negative"
        else:
            return "Neutral"
