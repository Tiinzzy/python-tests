import json
import urllib.request
import urllib.parse
import urllib.error
import collections
collections.Callable = collections.abc.Callable

serviceUrl = 'https://py4e-data.dr-chuck.net/comments_1703728.json'

while True:
    address = input('Enter URL: ')
    if len(address) < 1:
        break

    print('Retrieving ', address)
    uh = urllib.request.urlopen(address)
    data = uh.read().decode()

    try:
        js = json.loads(data)        
    except:
        js = None
        print('Something went wrong!')

    sum = 0
    for c in js['comments']:
        numbers = int(c['count'])
        sum += numbers
    
    print(sum)
