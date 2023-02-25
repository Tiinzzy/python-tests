from nltk.tokenize import wordpunct_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import ssl
import string
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import collections
collections.Callable = collections.abc.Callable


class NltkProcess:
    def __init__(self):
        pass

    @classmethod
    def open_and_read_url(self, url):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        try:
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'lxml')
            return soup
        except:
            return None

    @classmethod
    def init_web_page(self, url):
        soup = self.open_and_read_url(url)
        self.text = soup.get_text(separator=' ')
        return self

    @classmethod
    def tokenize(self, give_text=None):
        if give_text is None:
            give_text = self.text
        self.tokens = wordpunct_tokenize(give_text)
        return self

    @classmethod
    def remove_stop_words(self):
        all_stop_words = set(stopwords.words(
            'english') + list(string.punctuation))

        self.no_stop_word_tokens = []
        for t in self.tokens:
            if t.lower() not in all_stop_words:
                self.no_stop_word_tokens.append(t.lower())
        return self

    @classmethod
    def get_most_common_words(self, count, giev_tokens=None):
        if giev_tokens is None:
            giev_tokens = self.tokens
        self.frequency = FreqDist(giev_tokens)
        return self.frequency.most_common(count)

    @classmethod
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

    @classmethod
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

        plt.rcParams['figure.dpi'] = 300
        fig, ax = plt.subplots()
        ax.plot(xs, ys, "|")
        ax.set_yticks(list(range(len(words))), words, color="C0")
        ax.set_ylim(-1, len(words))
        ax.set_title(title)
        ax.set_xlabel("Word Offset")
        ax.set_xlim([0, len(self.tokens)])

        return fig

    @classmethod
    def get_text(self):
        for i in self.text:
            txt = ' '.join(self.text.split())
        return txt

    @classmethod
    def get_tokens(self):
        return self.tokens

    @classmethod
    def get_no_stop_words_tokens(self):
        return self.no_stop_word_tokens

    @classmethod
    def get_sample_chart_fig(self):
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)
        fig, ax = plt.subplots()
        ax.plot(t, s)
        ax.set(xlabel='time (s)', ylabel='voltage (mV)',
               title='About as simple as it gets, folks')
        ax.grid()
        return fig


if __name__ == "__main__":
    url = 'https://www.cnn.com/'
    NltkProcess.init_web_page(url).tokenize().remove_stop_words()

    # print(NltkProcess.get_text())
    # print('\n' * 2)
    # print(NltkProcess.get_tokens())
    # print('\n' * 2)
    # print(NltkProcess.get_no_stop_words_tokens())
    # print('\n' * 2)
    # print(NltkProcess.get_most_common_words(
    #     10, NltkProcess.get_no_stop_words_tokens()))
    # print('\n' * 2)
    # print(NltkProcess.get_frequency_as_data_frame())
    # print('\n' * 10)
    # print(NltkProcess.get_frequency_as_data_frame().head(5).values.tolist())

    NltkProcess.draw_lexical_dispersion_plot(["cnn", "news", "newsletters"])
