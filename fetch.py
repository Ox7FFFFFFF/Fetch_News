import urllib.request
import urllib.parse
import requests
import lxml
import html
import json
from bs4 import BeautifulSoup

# 聯合新聞網
url = "https://udn.com/rssfeed/hottest?ch=news"

html_doc = urllib.request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html_doc, 'html.parser')
searchlist = soup.find_all('item')
news_list=[]

server_url = 'http://127.0.0.1:8000/api/news/'
headers = {'Content-Type':'application/json'}

news_list=[]
for s in searchlist:
#     聯合新聞的拆法
    title = s.title.text
    link = s.guid.text
    tag = s.description.text
    t = BeautifulSoup(tag, 'html.parser')
    image = t.img['src']
    info = t.find_all('p')[1].text
    news_dict = {'title':title,'link':link,'image':image,'info':info}
    
    json_data = json.dumps(news_dict).encode('utf8')
    res = requests.post(server_url, json_data,headers = headers)
    print(res.content.decode())
#     news_list.append(news_dict)

# for index in range(len(news_obj)):
#     print("{} ".format(index)+news_obj[index].title);
