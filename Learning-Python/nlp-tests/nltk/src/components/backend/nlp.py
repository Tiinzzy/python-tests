from nltk.tokenize import wordpunct_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt
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
    def tokenize(self
                 ):
        self.tokens = wordpunct_tokenize(self.text)
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
    def process_text_file(self, text):
        print()
        print('>>>>>>>>>>>>>>>>>>>>>>>.', text)
        return {'result': 'rescieved'}


if __name__ == "__main__":
    url = 'https://www.cnn.com/'
    NltkProcess.init_web_page(url).tokenize().remove_stop_words()

    print(NltkProcess.get_text())
    print('\n' * 2)
    print(NltkProcess.get_tokens())
    print('\n' * 2)
    print(NltkProcess.get_no_stop_words_tokens())
    print('\n' * 2)
    print(NltkProcess.get_most_common_words(10, NltkProcess.get_no_stop_words_tokens()))
