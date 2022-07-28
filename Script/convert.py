# Python program to modify HTML
# with the help of Beautiful Soup

# Import the libraries
from bs4 import BeautifulSoup
import os
import re

def convert(file):
    #with open(os.path.join(base, 'CAT001EN.HTM'), 'r',encoding='ISO-8859-1', errors='ignore') as file_1:
    with open(file, 'r',encoding='GB2312', errors='ignore') as file_1:
        soup = BeautifulSoup(file_1, features='lxml')
        file_1.close()
        
        if soup.find("meta", content='text/html;charset=utf-8')==None:
            metatag = soup.new_tag('meta')
            metatag.attrs['http-equiv'] = 'Content-Type'
            metatag.attrs['content'] = 'text/html;charset=utf-8'
            soup.head.append(metatag)
            cap = soup.find("caption")
            if cap != None:
                cap.name = "p"
            
            with open(file, 'w') as file_1:
                file_1.write(soup.prettify())

base = "/Users/feizheng/Documents/GitHub/coachfei.github.io/liaoning2022/"
os.chdir(base)
for root, dirs, files in os.walk(base):
    for name in files:
        base,ext = os.path.splitext(name)
        if ext.lower() == '.htm':
            print(name)
            convert(name)
