from flask import Flask, request, jsonify
from nlp import NltkProcess
import base64

app = Flask(__name__)


@app.route("/url-to-txt-and-tokens", methods=['GET'])
def process_url():
    args = request.args
    url = args.get('url')
    main_url = base64.b64decode(url).decode('utf-8')

    NltkProcess.init_web_page(main_url).tokenize().remove_stop_words()

    text = NltkProcess.get_text()
    tokens = NltkProcess.get_tokens()
    nonStopWord = NltkProcess.get_no_stop_words_tokens()

    result = {'text': text, 'tokens': tokens, 'nonStopWord': nonStopWord}

    return jsonify(result)


@app.route("/file-to-txt-and-tokens", methods=['POST'])
def process_text_file():
    test = request.form.getlist('query')
    # print(test, '<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    res = NltkProcess.process_text_file(test)

    return jsonify(res)


@app.route("/get-common-words-count", methods=['GET'])
def get_common_words():
    args = request.args
    count = args.get('count')
    count = int(count)

    common_words = NltkProcess.get_most_common_words(
        count, NltkProcess.get_no_stop_words_tokens())

    result = {'common_words': common_words}

    return jsonify(result)
