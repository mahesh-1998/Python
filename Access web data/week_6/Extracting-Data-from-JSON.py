import xml.etree.ElementTree as ET
import urllib.parse,urllib.request,urllib.error
from bs4 import BeautifulSoup
import json

url = input("Enter - ")
xml = urllib.request.urlopen(url).read()
data = xml.decode()
data = json.loads(data)

i=0
s=0
l = len(data['comments'])
while i < l:
    s = s + data['comments'][i]['count']
    i = i + 1
    
print("Count: ",l)
print("Sum:",s)

