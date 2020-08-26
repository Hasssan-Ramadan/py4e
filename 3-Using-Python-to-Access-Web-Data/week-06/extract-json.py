import urllib.request
import json

url = input('Enter location: ')

res = urllib.request.urlopen(url).read().decode()

data = json.loads(res)

count = len(data['comments'])
total = 0
for comment in data['comments']:
    total += comment['count']

print('Retrieving', url)
print('Retrieved', len(res), 'characters')
print('Count:', count)
print('Sum:', total)