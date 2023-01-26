import urllib.request
import urllib.parse
import urllib.error
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.cnn.com/2023/01/26/us/tyre-nichols-memphis-thursday/index.html'
uh = urllib.request.urlopen(url, context=ctx)
html = uh.read().decode()

soup = BeautifulSoup(html, 'html.parser')
tags = soup('p')
for tag in tags:
    tag = str(tag)
    tag = tag.strip('<p ').strip('">').strip('</p')
    print(tag.split('">'))