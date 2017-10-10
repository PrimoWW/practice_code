"""
重点在于urllib.request.urlretrieve函数
参数 finename 指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
参数 reporthook 是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，
    我们可以利用这个回调函数来显示当前的下载进度。
参数 data 指 post 到服务器的数据，该方法返回一个包含两个元素的(filename, headers)元组，
    filename 表示保存到本地的路径，header 表示服务器的响应头。
"""

from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup
import sqlite3

def cbk(a, b, c):
    """
    回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    """
    per = 100 * a * b / c
    if per > 100:
        per = 100
    print("{0: 0.2f}%".format(per))


html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "lxml")
imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
urlretrieve(imageLocation, "logo.jpg", cbk)

