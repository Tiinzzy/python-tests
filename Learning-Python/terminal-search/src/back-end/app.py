from flask import Flask, request, jsonify
import json

from sentiment import Sentiment

app = Flask(__name__)


def get_parameters(req):
    return json.loads(req.data.decode('utf8').replace("'", '"'))


@app.route('/search/prompt', methods=["POST"])
def get_search_prompt():
    parameters = get_parameters(request)
    search_prompt = parameters['prompt']

    array_of_titles = Sentiment.find_news_titles(search_prompt)

    titles_sentiment, titles = Sentiment.process_title_sentiment(array_of_titles)
    prompt_sentiment = Sentiment.process_prompt_sentiment(search_prompt)

    search_prompt = ''
    return jsonify({'titles_sentiment': titles_sentiment, 'prompt_sentiment': prompt_sentiment,
                    'array_of_titles': titles})
