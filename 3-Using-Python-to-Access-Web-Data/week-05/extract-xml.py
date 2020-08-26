import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(data)
counts = tree.findall('.//count')

total = 0
for count in counts:
    total += int(count.text)

print('Retrieved', len(data), 'characters')
print('Count:', len(counts))
print('Sum:', total)
