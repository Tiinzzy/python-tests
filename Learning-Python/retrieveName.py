import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import ssl

#URL: https://py4e-data.dr-chuck.net/known_by_Kasandra.html

ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter URL...')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

def get_link(page_url, link_number):
    html = urllib.request.urlopen(page_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    link_tags = soup('a')

    if link_number <= len(link_tags):
        return link_tags[link_number-1].get('href')
    else:
        return None

start_link = 'https://py4e-data.dr-chuck.net/known_by_Kasandra.html'

for i in range(7):
    start_link = get_link(start_link, 18)
    print(i, start_link)
