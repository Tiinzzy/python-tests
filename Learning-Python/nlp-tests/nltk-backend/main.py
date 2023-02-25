import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


from flask import Flask, request, jsonify
from nlp import NltkProcess
import base64

app = Flask(__name__)


def get_nltk_processor(request):
    text = request.json['text']
    url = request.json['url']
    my_nltk_processor = NltkProcess()

    if url is not None:
        main_url = base64.b64decode(url).decode('utf-8')
        my_nltk_processor.init_web_page(
            main_url).tokenize().remove_stop_words()
    else:
        my_nltk_processor.tokenize(text).remove_stop_words()

    my_nltk_processor.get_tokens()
    my_nltk_processor.get_no_stop_words_tokens()
    return my_nltk_processor


@app.route("/url-to-txt-and-tokens", methods=['GET'])
def process_url():
    args = request.args
    url = args.get('url')
    main_url = base64.b64decode(url).decode('utf-8')

    my_nltk_processor = NltkProcess()
    my_nltk_processor.init_web_page(main_url).tokenize().remove_stop_words()
    text = my_nltk_processor.get_text()
    tokens = my_nltk_processor.get_tokens()
    nonStopWord = my_nltk_processor.get_no_stop_words_tokens()

    result = {'text': text, 'tokens': tokens, 'nonStopWord': nonStopWord}

    return jsonify(result)


@app.route("/file-to-txt-and-tokens", methods=['POST'])
def process_text_file():
    text = request.json['text']

    my_nltk_processor = NltkProcess()
    my_nltk_processor.tokenize(text).remove_stop_words()
    tokens = my_nltk_processor.get_tokens()
    no_stopwords = my_nltk_processor.get_no_stop_words_tokens()

    result = {'tokens': tokens, 'no_stopwords': no_stopwords}
    return jsonify(result)


@app.route("/get-common-words-count", methods=['POST'])
def get_common_words():
    count = request.json['count']
    count = int(count)

    my_nltk_processor = get_nltk_processor(request)
    common_words = my_nltk_processor.get_most_common_words(
        count, my_nltk_processor.get_no_stop_words_tokens())
    all_freq = len(my_nltk_processor.get_frequency_as_data_frame())

    result = {'common_words': common_words, 'all': all_freq}
    return jsonify(result)


@app.route("/get-frequency-of-words", methods=['POST'])
def get_frequency_of_words():
    count = request.json['count']
    count = int(count)

    my_nltk_processor = get_nltk_processor(request)
    freq = my_nltk_processor.get_frequency_as_data_frame()
    frequency = freq.head(count).values.tolist()
    result = {'freq': frequency}

    return jsonify(result)


@app.route("/get-graph-of-dispersion-plot", methods=['POST'])
def get_dispersion_plot():
    words = request.json['words']
    words = words.split(',')

    my_nltk_processor = get_nltk_processor(request)
    figure, base64_data = my_nltk_processor.draw_lexical_dispersion_plot(words)
    print(base64_data)
    return jsonify({'image': base64_data})


@app.route("/get-all-tokens-for-graph", methods=['POST'])
def get_all_tokens_for_graph():
    my_nltk_processor = get_nltk_processor(request)
    clean_tokens = my_nltk_processor.get_no_stop_words_tokens()
    result = {'cleanTokens': clean_tokens}
    return jsonify(result)


@app.route("/get-sample-chart", methods=['GET'])
def get_sample_chart():
    print('Hi THERE !!!')

    my_nltk_processor = NltkProcess()
    figure = my_nltk_processor.get_sample_chart_fig()
    output = io.BytesIO()
    FigureCanvas(figure).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
