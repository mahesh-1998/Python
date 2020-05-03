import urllib.parse, urllib.error, urllib.request
from bs4 import BeautifulSoup
import ssl
import re

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL ")
count = input("Enter count: ") 
pos = input("Enter position: ")
count = int(count)
pos = int(pos)

 #retrive all anchor tags
i = 0
sequence = list()
while i < pos:
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser') 
    #retrive all anchor tags
    tags = soup('a')
    print("Retrieving: "+url)
    c = 0
    for tag in tags:
        c = c + 1
        if(c == count):
            sequence.append(tag.get('href',None))
            url = sequence[i]
            break
    i = i + 1
    
print("Sequence of names:")
last_name = ""
n = 0
for name in sequence:
    print(str(re.findall('known_by_([a-zA-z]+)',name)))
    n = n + 1
    if n == len(sequence):
        last_name = str(re.findall('known_by_([a-zA-z]+)',name))
    
print("last name: ",last_name)
    


    