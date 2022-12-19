import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import ssl

#URL: https://py4e-data.dr-chuck.net/comments_1703725.html

ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL...')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
lst = list()
sum = 0
for tag in tags:
    num = tag.contents[0]
    sum += int(num)
print (sum)
