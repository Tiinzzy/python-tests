from flask import Flask, request, jsonify
from nlp import NltkProcess
import base64

app = Flask(__name__)


@app.route("/url-to-txt-and-tokens", methods=['GET'])
def top_ten_movies():
    args = request.args
    url = args.get('url')
    main_url = base64.b64decode(url).decode('utf-8')

    NltkProcess.init_web_page(main_url).tokenize().remove_stop_words()

    text = NltkProcess.get_text()
    tokens = NltkProcess.get_tokens()
    nonStopWord = NltkProcess.get_no_stop_words_tokens()

    result = {'text': text, 'tokens': tokens, 'nonStopWord': nonStopWord}

    return jsonify(result)
