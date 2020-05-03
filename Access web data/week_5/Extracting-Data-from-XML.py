import xml.etree.ElementTree as ET
import urllib.parse,urllib.request,urllib.error
from week 3.bs4 import BeautifulSoup

url = input("Enter - ")
xml = urllib.urlrequest.urlopen(url).read()
soup = BeautifulSoup(xml,'xml.parser')

print(soup)