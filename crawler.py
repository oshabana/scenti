from lxml import html
from html.parser import HTMLParser
import urllib, re
from bs4 import BeautifulSoup
import requests
from googlesearch import search



def retrive_data(google):
    text_data = "" 
    for url in search(google,stop=5):
        #print(url)
        try:
            html = urllib.request.urlopen(url)
            code = BeautifulSoup(html,"lxml")
            data = code.find(text=True)
            print(analyze(code))
            if analyze(text_from_html(code)):
                text_data = text_data + text_from_html(code)
            
        except Exception:
            pass
    
        #page = requests.get(url)
       # data = page.content
    return text_data
    
def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)
    
# def analyze(data):
#     parser = HTMLParser()
#     text = ""
#     for tag in data:
#         text = parser.handle_starttag(tag,data)
#         print(tag)
#     return text

def analyze(element):
     if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
         return False
     elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
     return True
       

print(retrive_data('dogs'))