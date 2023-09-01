import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")


class NLTKSentiment:

    @staticmethod
    def find_news_titles(search_prompt):
        base_url = "https://search.brave.com/news"
        params = {
            "q": search_prompt
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        links = []

        for anchor in soup.find_all("a"):
            title = anchor.get_text()
            link = anchor["href"]

            if link.startswith("http"):
                revised_title = title.replace('\n', ' * ').split(' * ')[-1]
                links.append({"title": revised_title})

        return links

    @staticmethod
    def process_title_sentiment(titles):
        num_to_save = min(len(titles), 10)
        news_to_save = titles[:num_to_save]

        title_texts = []
        for item in news_to_save:
            title_texts.append(item['title'])

        all_titles = ' '.join(title_texts)

        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(all_titles)

        if sentiment_scores['compound'] >= 0.05:
            return "Positive", title_texts
        elif sentiment_scores['compound'] <= -0.05:
            return "Negative", title_texts
        else:
            return "Neutral", title_texts

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
