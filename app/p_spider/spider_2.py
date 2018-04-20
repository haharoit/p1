# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
"""
爬虫实战二
网址：http://www.biqukan.com/1_1094/
内容：笔趣阁小说一念永恒
本次内容：爬取目录及各章链接
更新日期：2018-04-20
"""
if __name__ == "__main__":
    # 笔趣阁网站
    server = 'http://www.biqukan.com/'
    # 目标网址 一念永恒目录页
    target = 'http://www.biqukan.com/1_1094/'
    # request 请求
    req = requests.get(target)
    # 得到html
    html = req.text
    # 用BeautifulSoup解析html
    div_bf = BeautifulSoup(html, "html.parser")
    # 取 class 为 listmain 的 div
    div = div_bf.find_all('div', class_='listmain')
    # 打印
    # print(div[0])
    # 用BeautifulSoup解析div
    a_bf = BeautifulSoup(str(div[0]), "html.parser")
    # 取 a 为 各章节 链接
    a = a_bf.find_all('a')
    # 把章节名和链接组合
    for e in a:
        print e.string, server + e.get('href')