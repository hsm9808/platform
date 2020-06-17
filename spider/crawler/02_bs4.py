# -*- coding:utf8   -*-
# @Author :George华
# @Time : 2020/6/15 2:21 下午


from bs4 import BeautifulSoup
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.baidu.com"

req = urllib.request.urlopen(url=url)

response = req.read().decode("utf-8")

bs = BeautifulSoup(response, "html.parser")

m_list = bs.find_all("html")
print(m_list)
