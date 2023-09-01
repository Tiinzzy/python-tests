import requests
from bs4 import BeautifulSoup
from textblob import TextBlob


class TextBlobSentiment:

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
