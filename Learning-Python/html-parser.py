from lxml import html
from lxml import etree
import requests


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


def look_for_p(element):
    for el in element:
        print(str(el)[:100])
        # if str(el).startswith('<p'):
        #     print(str(el)[:100])


if __name__ == "__main__":
    parser = etree.HTMLParser()
    context = etree.iterparse('/var/tmp/test.html', parser)

    for action, elem in context:
        print (action, elem.tag)