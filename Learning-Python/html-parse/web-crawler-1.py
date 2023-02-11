import sys
import random
from database import Database
import ssl
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import collections

collections.Callable = collections.abc.Callable


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

SECION_TAG = 'section'
SECION_CLASSES = ['module', 'module--news', 'module--collapse-images']

NEWS_TAG = 'div'
NEWS_CLASSES = ['module__content']

ANCHOR_TAG = 'a'

already_seen_urls = []

def get_page(url):
    try:
        html = urllib.request.urlopen(start_link, context=ctx).read()
        soup = BeautifulSoup(html, 'lxml')
        return html, soup
    except:
        return None, None


def is_a_tag(element, tag_id):
    is_tag = (element.name == tag_id)
    return is_tag


def tag_has_classes(element, classes):
    has_classes = True
    for cls in classes:
        if 'class' in element.attrs.keys():
            element_classes = element.attrs['class']
            if cls not in element_classes:
                has_classes = False
        else:
            has_classes = False

    return has_classes


def is_a_tag_with_classes(element, tag, classes):
    if is_a_tag(element, tag):
        if tag_has_classes(element, classes):
            return True
    return False


def test_1(start_link):
    html, soup = get_page(start_link)

    section_found = False
    news_found = False
    for chld in soup.recursiveChildGenerator():
        if not news_found:
            if not section_found and is_a_tag_with_classes(chld, SECION_TAG, SECION_CLASSES):
                section_found = True
            if section_found and is_a_tag_with_classes(chld, NEWS_TAG, NEWS_CLASSES):
                news_found = True
                print('------------------------>\n')
                print(chld)
                print('\n<------------------------')


def get_anchor_href(element):
    if 'href' in element.attrs.keys():
        return element.attrs['href']
    else:
        return None


def get_url_hrefs(url, count):
    base_url = url[:-1] if url.endswith('/') else url
    urls = []
    html, soup = get_page(url)
    for chld in soup.recursiveChildGenerator():
        if is_a_tag(chld, ANCHOR_TAG):
            href = get_anchor_href(chld)
            if href is not None and not href.startswith('#'):
                href = href if href.startswith('http') else base_url + href
                if href not in already_seen_urls:                    
                    already_seen_urls.append(href)
                    urls.append(href)

    return random.choices(urls, k=count)


def crawl(given_urls, depth, count, level):
    if level > depth:
        return
    for gurl in given_urls:
        print(str(level)+('-'*2*level)+'>', gurl)
        drived_urls = get_url_hrefs(gurl, count)
        crawl(drived_urls, depth, count, level+1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_link = sys.argv[1]
    else:
        # start_link = input('Please enter a wikipedia link: ')
        start_link = 'https://en.wikipedia.org/wiki/jazz'

    crawl([start_link], depth=3, count=5, level=0)
