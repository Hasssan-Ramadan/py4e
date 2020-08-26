import urllib.request, urllib.parse
import json

base_url = 'http://py4e-data.dr-chuck.net/json?'

params = dict()
params['key'] = 42
params['address'] = input('Enter location: ')

url = base_url + urllib.parse.urlencode(params)
print('Retrieving', url)

res = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(res), 'characters')

place_id = json.loads(res)['results'][0]['place_id']
print('Place id', place_id)
