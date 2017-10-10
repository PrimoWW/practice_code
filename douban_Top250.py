"""
爬了豆瓣Top250的电影名字，主要有以下几个注意点
1：.select方法返回的是list
    .find返回的是bs4.element.tag
    在处理单个对象的时候.find比.select方便不少
2.通过循环写入文件的时候，要用"a"打开，"w"会覆盖原来的东西
3.对列表，字典，字符串的处理还是不熟练
"""
from bs4 import BeautifulSoup
import requests

filename = "E:/douban_Top250/top250.txt"
douban_url = "https://movie.douban.com/top250/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36"
}


def get_soup(url):
    response = requests.get(url, headers)
    soup = BeautifulSoup(response.text, "lxml")
    titles = soup.select("div.hd > a > span:nth-of-type(1)")
    next_page = soup.find("span", attrs={"class": "next"}).find("a")

    movie_names = []

    for title in titles:
        movie_name = title.string
        movie_names.append(movie_name)

    if next_page:
        return movie_names, "https://movie.douban.com/top250" + next_page.get("href")
    else:
        return movie_names, None


all_names = []

while douban_url:
    part_names, douban_url = get_soup(douban_url)

    for name in part_names:
        all_names.append(name)

    with open(filename, "a") as file_object:
        for name in part_names:
            file_object.write(name + "\n")
        file_object.close()

print(all_names)