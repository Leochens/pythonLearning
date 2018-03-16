#coding:utf-8
import requests
from bs4 import  BeautifulSoup
import lxml

url = 'http://blog.mokis.top'

data = requests.request('GET',url)

#print(''.join([li for li in data.headers]))

print(data.headers)
