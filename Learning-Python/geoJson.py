import json
import urllib.request
import urllib.parse
import urllib.error
import ssl
import collections
collections.Callable = collections.abc.Callable

api_key = False

if api_key is False :
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print(data)
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
        print('Something went wrong!')

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    
    id = js['results'][0]['place_id']
    print('place id: ', id)