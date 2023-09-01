from flask import Flask, request, jsonify
import json
import requests
from bs4 import BeautifulSoup

from nltk_sentiment import NLTKSentiment
from textblob_sentiment import TextBlobSentiment
from vader_sentiment import VaderSentiment

app = Flask(__name__)


def get_all_ten_titles(prompt):
    base_url = "https://search.brave.com/news"
    params = {
        "q": prompt
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

    num_to_save = min(len(links), 10)
    news_to_save = links[:num_to_save]

    title_texts = []
    for item in news_to_save:
        title_texts.append(item['title'])

    all_titles = ' '.join(title_texts)

    return all_titles, title_texts


def get_parameters(req):
    return json.loads(req.data.decode('utf8').replace("'", '"'))


@app.route('/search/prompt', methods=["POST"])
def get_search_prompt():
    parameters = get_parameters(request)
    search_prompt = parameters['prompt']

    all_titles_as_text, array_of_titles = get_all_ten_titles(search_prompt)

    nltk_titles_sentiment, nltk_score = NLTKSentiment.process_title_sentiment(all_titles_as_text)
    nltk_prompt_sentiment = NLTKSentiment.process_prompt_sentiment(search_prompt)

    text_blob_titles_sentiment, text_blob_score = TextBlobSentiment.process_title_sentiment(all_titles_as_text)
    text_blob_prompt_sentiment = TextBlobSentiment.process_prompt_sentiment(search_prompt)

    vader_titles_sentiment, vader_score = VaderSentiment.process_title_sentiment(all_titles_as_text)
    vader_prompt_sentiment = VaderSentiment.process_prompt_sentiment(search_prompt)

    search_prompt = ''
    return jsonify({'nltk_titles_sentiment': nltk_titles_sentiment, 'nltk_prompt_sentiment': nltk_prompt_sentiment,
                    'nltk_score': nltk_score, 'array_of_titles': array_of_titles,
                    'text_blob_titles_sentiment': text_blob_titles_sentiment,
                    'text_blob_prompt_sentiment': text_blob_prompt_sentiment, 'text_blob_score': text_blob_score,
                    'vader_titles_sentiment': vader_titles_sentiment, 'vader_score': vader_score,
                    'vader_prompt_sentiment': vader_prompt_sentiment, 'array_of_titles': array_of_titles})
