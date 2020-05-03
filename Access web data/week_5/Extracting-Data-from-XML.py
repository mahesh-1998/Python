import xml.etree.ElementTree as ET
import urllib.parse,urllib.request,urllib.error
from bs4 import BeautifulSoup

url = input("Enter - ")
xml = urllib.request.urlopen(url).read()
tree = ET.fromstring(xml)
counts = tree.findall('.//count')
c = 0
s = 0
for count in counts:
    s = s + int(count.text)
    c = c + 1

print("Count: ",c)
print("Sum:",s)