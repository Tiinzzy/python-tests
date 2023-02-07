import re
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


def get_link(start_link):
    lines = list()
    html = urllib.request.urlopen(start_link, context=ctx).read()
    soup = BeautifulSoup(html, 'lxml')
    for child in soup.recursiveChildGenerator():
        if child.name == 'div' and {'class': 'mw-parser-output'}:
            for ch in child:
                if str(ch).startswith('<p'):
                    lines.append(str(ch).split('<p>'))
    wikipedia_link = ''
    link = lines[2]
    for l in link:
        leftKey = '<a '
        rightKey = '" title'
        str_l = str(l)
        wiki = str_l[str_l.find(leftKey):]
        wiki_link = wiki[:wiki.find(rightKey)]
        # print('>>>>>>>>>>>', wiki_link)
        final_link = wiki_link[-100:]
        final = final_link[final_link.find('href="')+6:]
        # print('>>>>', final)
        wiki_orig = 'https://en.wikipedia.org'
        wikipedia_link = wiki_orig + final
    return wikipedia_link


def do_search(start_link):
    if start_link is None:
        start_link = input('Please enter a wikipedia link: ')

    for i in range(25):
        start_link = get_link(start_link)
        print('>>>>>>>>>>>', i, start_link)
        print('')
        if re.search('Philosophy', start_link):
            break   


if __name__ == "__main__":
    start_link = input('Please enter a wikipedia link: ')
    do_search(start_link)
