#coding:utf-8
import requests
from bs4 import  BeautifulSoup
import lxml

#使用requests简单爬去图片


img_url='http://c.jeeok.com/images/keyu/1.jpg'

data = requests.get(img_url)

with open('pic.jpg','wb') as file:
    file.write(data.content)
