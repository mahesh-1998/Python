import urllib.parse, urllib.error, urllib.request
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter -")
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')
 
 #retrive all anchor tags
s = 0
c = 0
tags = soup('span')
for tag in tags:
    s = s + int(tag.contents[0])
    c = c + 1
print("count:",c)
print("sum:",s)