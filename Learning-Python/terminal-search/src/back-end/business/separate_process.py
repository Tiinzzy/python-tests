import requests
from bs4 import BeautifulSoup
import re

from .sentiment.nltk_sentiment import NLTKSentiment
from .sentiment.textblob_sentiment import TextBlobSentiment
from .sentiment.vader_sentiment import VaderSentiment


def get_separate_ten_titles(prompt):
    base_url = "https://search.brave.com/news"
    params = {
        "q": prompt
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    links = []
    cleaned_data = []

    for anchor in soup.find_all("a"):
        title = anchor.get_text()
        link = anchor["href"]
        if link.startswith("http"):
            revised_title = title.replace('\n', ' * ').split(' * ')[-1]
            links.append({"title": revised_title})

    for item in links:
        cleaned_title = re.sub(r'^[^•]+•\s+', '', item['title'])
        cleaned_title = re.sub(r'\d+\s+day[s]? ago\s+', '', cleaned_title)
        cleaned_data.append({'title': cleaned_title.strip()})

    num_to_save = min(len(cleaned_data), 10)
    news_to_save = cleaned_data[:num_to_save]

    return news_to_save


def process_sentiment_separately(array_of_titles):
    nltk_step_sentiment = NLTKSentiment.process_prompt_one_by_one_sentiment(array_of_titles)

    text_blob_step_sentiment = TextBlobSentiment.process_prompt_one_by_one_sentiment(array_of_titles)

    vader_step_sentiment = VaderSentiment.process_prompt_one_by_one_sentiment(array_of_titles)

    return {'nltk_step_sentiment': nltk_step_sentiment, 'text_blob_step_sentiment': text_blob_step_sentiment,
            'vader_step_sentiment': vader_step_sentiment}
