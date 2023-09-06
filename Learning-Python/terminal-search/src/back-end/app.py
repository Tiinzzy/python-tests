from flask import Flask, request, jsonify
import json

from business.total_process import get_all_ten_titles, process_sentiment_for_all
from business.separate_process import get_separate_ten_titles, process_sentiment_separately
from business.classifier_process import get_vector_classification_result

app = Flask(__name__)


def get_parameters(req):
    return json.loads(req.data.decode('utf8').replace("'", '"'))


@app.route('/search/prompt', methods=["POST"])
def get_search_prompt():
    parameters = get_parameters(request)
    search_prompt = parameters['prompt']
    selected = parameters['msg']

    if selected == 'all':
        all_titles_as_text, array_of_titles = get_all_ten_titles(search_prompt)
        finished_process = process_sentiment_for_all(search_prompt, all_titles_as_text)

        return jsonify({'all_ten': True, 'array_of_titles': array_of_titles, 'data': finished_process})
    else:
        pass
        array_of_titles = get_separate_ten_titles(search_prompt)
        finished_data = process_sentiment_separately(array_of_titles)

        return jsonify(finished_data)


@app.route('/vector/classifier', methods=["POST"])
def get_classifying_text():
    parameters = get_parameters(request)
    text = parameters['text']
    result = get_vector_classification_result(text)
    print(result)

    return jsonify({'result': True})
