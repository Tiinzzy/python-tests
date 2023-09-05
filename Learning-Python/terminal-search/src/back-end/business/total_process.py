from .sentiment.nltk_sentiment import NLTKSentiment
from .sentiment.textblob_sentiment import TextBlobSentiment
from .sentiment.vader_sentiment import VaderSentiment

import requests
from bs4 import BeautifulSoup
import re


def get_all_ten_titles(prompt):
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

    title_texts = []
    for item in news_to_save:
        title_texts.append(item['title'])

    all_titles = ' '.join(title_texts)

    return all_titles, title_texts


def process_sentiment_for_all(search_prompt, all_titles_as_text):
    nltk_titles_sentiment, nltk_score = NLTKSentiment.process_title_sentiment(all_titles_as_text)
    nltk_prompt_sentiment = NLTKSentiment.process_prompt_sentiment(search_prompt)

    text_blob_titles_sentiment, text_blob_score = TextBlobSentiment.process_title_sentiment(all_titles_as_text)
    text_blob_prompt_sentiment = TextBlobSentiment.process_prompt_sentiment(search_prompt)

    vader_titles_sentiment, vader_score = VaderSentiment.process_title_sentiment(all_titles_as_text)
    vader_prompt_sentiment = VaderSentiment.process_prompt_sentiment(search_prompt)

    return {'nltk_titles_sentiment': nltk_titles_sentiment, 'nltk_prompt_sentiment': nltk_prompt_sentiment,
            'nltk_score': nltk_score, 'text_blob_titles_sentiment': text_blob_titles_sentiment,
            'text_blob_prompt_sentiment': text_blob_prompt_sentiment, 'text_blob_score': text_blob_score,
            'vader_titles_sentiment': vader_titles_sentiment, 'vader_score': vader_score,
            'vader_prompt_sentiment': vader_prompt_sentiment}
