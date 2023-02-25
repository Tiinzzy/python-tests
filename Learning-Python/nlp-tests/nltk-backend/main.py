import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


from flask import Flask, request, jsonify
from nlp import NltkProcess
import base64

app = Flask(__name__)

nltk_processor = NltkProcess()


@app.route("/url-to-txt-and-tokens", methods=['GET'])
def process_url():
    args = request.args
    url = args.get('url')
    main_url = base64.b64decode(url).decode('utf-8')

    nltk_processor.init_web_page(main_url).tokenize().remove_stop_words()

    text = nltk_processor.get_text()
    tokens = nltk_processor.get_tokens()
    nonStopWord = nltk_processor.get_no_stop_words_tokens()

    result = {'text': text, 'tokens': tokens, 'nonStopWord': nonStopWord}

    return jsonify(result)


@app.route("/file-to-txt-and-tokens", methods=['POST'])
def process_text_file():
    text = request.json['text']

    nltk_processor.tokenize(text).remove_stop_words()

    tokens = nltk_processor.get_tokens()
    no_stopwords = nltk_processor.get_no_stop_words_tokens()

    result = {'tokens': tokens, 'no_stopwords': no_stopwords}
    return jsonify(result)


@app.route("/get-common-words-count", methods=['GET'])
def get_common_words():
    args = request.args
    count = args.get('count')
    count = int(count)

    common_words = nltk_processor.get_most_common_words(
        count, nltk_processor.get_no_stop_words_tokens())
    all_freq = len(nltk_processor.get_frequency_as_data_frame())

    result = {'common_words': common_words, 'all': all_freq}

    return jsonify(result)


@app.route("/get-frequency-of-words", methods=['GET'])
def get_frequency_of_words():
    args = request.args
    count = args.get('count')
    count = int(count)

    freq = nltk_processor.get_frequency_as_data_frame()
    frequency = freq.head(count).values.tolist()
    result = {'freq': frequency}

    return jsonify(result)


@app.route("/get-graph-of-dispersion-plot", methods=['GET'])
def get_dispersion_plot():
    args = request.args
    words = args.get('words')
    words = words.split(',')
    figure = nltk_processor.draw_lexical_dispersion_plot(words)
    output = io.BytesIO()
    FigureCanvas(figure).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route("/get-sample-chart", methods=['GET'])
def get_sample_chart():
    print('Hi THERE !!!')
    figure = nltk_processor.get_sample_chart_fig()
    output = io.BytesIO()
    FigureCanvas(figure).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
