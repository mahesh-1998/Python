import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://python-data.dr-chuck.net/json'
address = input('Enter location: ')
url = serviceurl + '?' + urllib.parse.urlencode({'address':  address, 'key': 42})
data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)
info = info['results']
print ('Retrieving', url, '\nRetrieved', len(data), 'caracters')
for item in info:
    key = item['place_id']
print ('Place id:', key)