import sys
import re
import ssl
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import collections
collections.Callable = collections.abc.Callable

MAX_DEPTH = 100
WIKI_BASE_URL = 'https://en.wikipedia.org'


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_url_from_tag(tag_str):
    key = ' href="'
    start = tag_str.strip().lower().index(key)
    link = tag_str[start+len(key):]
    key = '"'
    end = link.strip().lower().index(key)
    link = link[:end]
    link = WIKI_BASE_URL + link
    return link


def get_link(page_url, link_number):
    html = urllib.request.urlopen(page_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    divTag = soup.find("div", {"class": "mw-parser-output"})


    children = divTag.findChildren()
    for c in children:
        if str(c).startswith('<p'):
            print(c)
            print('............................')

    index = None
    link = None
    for tag in divTag:
        pTags = tag.find_all("p")
        for tag in pTags:
            tag_str = str(tag)
            try:
                index = tag_str.strip().lower().index('<p>')
                if index == 0:
                    link = get_url_from_tag(tag_str)
                    break
            except:
                pass

    return link


def get_wiki_title(url):
    # url = https://en.wikipedia.org/wiki/Empirical_evidence
    # return empirical_evidence
    return ""


def add_to_database(from_title, to_title):
    # check if you arleady have (from_title, to_title) return false, do nothing

    # insert into some table (from_title, to_title)
    # you may name table as title_relations
    # return true
    pass


def do_search(start_link):
    if start_link is None:
        start_link = input('Please enter a wikipedia link: ')

    from_tile = get_wiki_title(start_link)
    for i in range(MAX_DEPTH):
        start_link = get_link(start_link, 1)
        to_title = get_wiki_title(start_link)
        add_to_database(from_tile, to_title)
        from_tile = to_title

        print(i, start_link)
        if re.search('Philosophy', start_link):
            break


if __name__ == "__main__":
    # do_search(sys.argv[1])
    do_search("https://en.wikipedia.org/wiki/Felinae")
