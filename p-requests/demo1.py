#coding:utf-8
import requests
from bs4 import  BeautifulSoup
import lxml

url = 'http://blog.mokis.top'

data = requests.request('GET',url)

#print(''.join([li for li in data.headers]))

print('打印请求头:')
print(data.headers)

print('打印状态码')
print(data.status_code)

print('打印文本')
print(data.text)

print('打印转义后字符串')
print(data.content)

print('打印编码格式')
print(data.encoding)

print('打印返回解析的响应头部链接（如果有的话）。')
print(data.links)

print('打印请求')
print(data.request)

print(data.cookies)

print(data.json)