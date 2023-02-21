from nltk.tokenize import wordpunct_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt
from nltk.text import Text
import string
import ssl
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import collections
collections.Callable = collections.abc.Callable


DOCUMENT_FOLDER = '/home/tina/Documents/python/python-tests/Learning-Python/nlp-tests/'


class NltkProcess:
    def __init__(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

    def init_by_file(self, file_name):
        text_file = open(DOCUMENT_FOLDER + file_name, 'r')
        self.text = text_file.read()
        return self

    def __open_and_read_url(self, url):
        try:
            html = urllib.request.urlopen(url, context=self.ctx).read()
            soup = BeautifulSoup(html, 'lxml')
            return soup
        except:
            return None

    def init_web_page(self, url):
        soup = self.__open_and_read_url(url)
        self.text = soup.get_text(separator=' ')
        return self

    def tokenize(self):
        self.tokens = wordpunct_tokenize(self.text)
        return self

    def get_most_common_words(self, count, giev_tokens=None):
        if giev_tokens is None:
            giev_tokens = self.tokens
        self.frequency = FreqDist(giev_tokens)
        return self.frequency.most_common(count)

    def get_frequency_as_data_frame(self):
        words = []
        frequency = []
        for w in self.frequency.keys():
            words.append(w)
            frequency.append(self.frequency.freq(w)*100)
        df = pd.DataFrame()
        df['words'] = words
        df['frequency'] = frequency
        df = df.sort_values(by=['frequency'], ascending=False)
        return df

    def remove_stop_words(self):
        all_stop_words = set(stopwords.words(
            'english') + list(string.punctuation))

        self.no_stop_word_tokens = []
        for t in self.tokens:
            if t.lower() not in all_stop_words:
                self.no_stop_word_tokens.append(t.lower())
        return self

    def draw_lexical_dispersion_plot(self, words, ignore_case=False, title="Lexical Dispersion Plot"):
        word2y = {
            word.casefold() if ignore_case else word: y
            for y, word in enumerate(reversed(words))
        }
        xs, ys = [], []
        for x, token in enumerate(self.tokens):
            token = token.casefold() if ignore_case else token
            y = word2y.get(token)
            if y is not None:
                xs.append(x)
                ys.append(y)

        _, ax = plt.subplots()
        ax.plot(xs, ys, "|")
        ax.set_yticks(list(range(len(words))), words, color="C0")
        ax.set_ylim(-1, len(words))
        ax.set_title(title)
        ax.set_xlabel("Word Offset")
        ax.set_xlim([0, len(self.tokens)])

        plt.show()
        return ax

    def show_concordance(self, word):
        text = Text(self.tokens)
        text.concordance(word)

    def get_collocation(self):
        text = Text(self.tokens)
        result = text.collocation_list()
        return result

    def get_simillarities(self, word):
        text = Text(self.tokens)
        result = text.similar(word)
        return result

    def get_text(self):
        for i in self.text:
            txt = ' '.join(self.text.split())
        return txt

    def get_tokens(self):
        return self.tokens

    def get_no_stop_words_tokens(self):
        return self.no_stop_word_tokens


if __name__ == "__main__":
    myNlpDoc = NltkProcess()

    myNlpDoc.init_web_page(
        'https://www.foxnews.com/').tokenize().remove_stop_words()
    # myNlpDoc.init_by_file('text.txt').tokenize().remove_stop_words()

    print(myNlpDoc.get_text())
    print('\n' * 2)
    print(myNlpDoc.get_tokens())
    print('\n' * 2)
    print(myNlpDoc.get_most_common_words(5))
    print('\n' * 2)
    print(myNlpDoc.get_no_stop_words_tokens())
    print('\n' * 2)
    print(myNlpDoc.get_most_common_words(
        5, myNlpDoc.get_no_stop_words_tokens()))
    print('\n' * 2)
    print(myNlpDoc.get_frequency_as_data_frame().head(10))
    print('\n' * 2)
    print(myNlpDoc.get_collocation())
    print('\n' * 2)
    print(myNlpDoc.get_simillarities('news'))
    print('\n' * 2)
    # myNlpDoc.show_concordance('news')
    print('\n' * 2)


    # myNlpDoc.draw_lexical_dispersion_plot(["guardian", "want", "ai", "says", "programming","news", 'chatbots'])

