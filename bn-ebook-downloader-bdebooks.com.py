import requests as REQ
import xml.etree.ElementTree as ET
import urllib.parse
import os

x = REQ.get('https://dl.bdebooks.com/')
root = ET.fromstring(x.content)
length = len(root.getchildren())
print(length)
for i in range(6, length):
    file = root[i][0].text
    pre_url = urllib.parse.quote(file)
    print(root[i][0].text)
    url = ('https://dl.bdebooks.com/%s' %pre_url)
    print(url)
    file2 =file.split('/')[-1]
    print(file2)
    

      
    
    if file2.endswith('.pdf'):
        r = REQ.get(url, stream = True)
        with open('/your_directory/%s'%file2, 'wb') as Pypdf: #Add your real directory in the place of "your_directory" where the file to be saved
            
            for chunk in r.iter_content(chunk_size = 1024):

                if chunk:

                    Pypdf.write(chunk)
    
    else:  
            continue

    
    
