import ssl
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import collections
collections.Callable = collections.abc.Callable


class Nltk_Process:
    def __init__(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

    def open_and_read_text(self, text):
        text_file = open(
            '/home/tina/Documents/python/python-tests/Learning-Python/nlp-tests/' + text, 'r')
        txt = text_file.read()
        result = print(txt)
        return result

    def open_and_read_url(self, url):
        try:
            html = urllib.request.urlopen(url, context=self.ctx).read()
            soup = BeautifulSoup(html, 'lxml')
            return soup
        except:
            return None

    def read_web_page(self, url):
        soup = self.open_and_read_url(url)
        text = soup.get_text()
        result = print(text)
        return result


if __name__ == "__main__":
    test = Nltk_Process()
    # test.open_and_read_text('text.txt')
    test.read_web_page('https://www.foodnetwork.ca/recipe/air-fryer-cauliflower-bites/')
