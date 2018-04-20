# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
"""
爬虫实战三
网址：http://www.biqukan.com/1_1094/
内容：笔趣阁小说一念永恒
本次内容：爬取目录及各章链接
更新日期：2018-04-20
"""


class downloader(object):

    # 初始化
    def __init__(self):
        self.base = 'http://www.biqukan.com/'
        self.begin = 'http://www.biqukan.com/1_1094'
        self.names = []   # 存放章节名
        self.urls = []    # 存放章节链接
        self.nums = []    # 存放章节数

    """
    获取章节链接
    Parameters:no
    Returns:no
    Modify:2018-04-20
    """
    def get_chapter(self):
        # request
        req = requests.get(self.begin)
        # 取 html
        html = req.text
        # 用BeautifulSoup解析html
        div_bf = BeautifulSoup(html, "html.parser")
        # 取div
        div = div_bf.find_all('div', class_='listmain')
        # 解析div
        a_bf = BeautifulSoup(str(div[0]), "html.parser")
        # 取a
        a = a_bf.find_all('a')
        # 剔除不必要的章节，计数
        self.nums = len(a[15:])
        for e in a[15:]:
            self.names.append(e.string)
            self.urls.append(self.base + e.get('href'))

    """
    获取章节内容
    Parameters：begin-下载链接(string)
    Returns:texts-章节内容(string)
    Modify:2018-04-20
    """
    def get_contents(self, begin):
        # request
        req = requests.get(begin)
        # 取html
        html = req.text
        # 解析html
        bf = BeautifulSoup(html, "html.parser")
        # 取div
        texts = bf.find_all('div', class_='showtxt')
        # div 取 内容 text 去空格 换行
        texts = texts[0].text.replace('\xa0'.decode("unicode_escape")*8, '\n\n')
        # 返回 内容
        return texts

    """
    将爬取的文章内容写入文件
    Parameters:
        name-章节名(string)
        path-小说保存路径及名称(string)
        text-章节内容(string)
    Returns:no
    Modify:2018-04-20
    """
    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a') as f:
            f.write(name + '\n')
            f.write(text)
            f.write('\n\n')


if __name__ == "__main__":
    dl = downloader()
    dl.get_chapter()
    print('《一念永恒》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i].encode("unicode_escape"), '一念永恒.txt'.decode("unicode_escape"), dl.get_contents(dl.urls[i]))
        sys.stdout.write("==========已下载：%.3f%%" % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《一念永恒》下载完成')


