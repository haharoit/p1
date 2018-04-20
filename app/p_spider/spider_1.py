# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
"""
爬虫实战一
网址：http://www.biqukan.com/1_1094/5403177.html
内容：笔趣阁小说一念永恒
本次内容：爬取第一章内容
更新日期：2018-04-20
"""
if __name__ == "__main__":
    # 第一章网址
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    # request 获取 返回内容
    req = requests.get(target)
    # 从返回内容里面 获取 html
    html = req.text
    # 用BeautifulSoup解析html
    bf = BeautifulSoup(html, "html.parser")
    # 获取div中class为showtxt的内容
    texts = bf.find_all('div', class_='showtxt')
    # 打印
    # print texts[0].text
    # 去空格，分段
    print texts[0].text.replace('\xa0'.decode("unicode_escape")*8, '\n\n')

