from bs4 import BeautifulSoup
import requests
import re
import time


url = "http://www.xiaohuar.com/2014.html"
url_10 = ["http://www.xiaohuar.com/list-1-{}.html".format(str(i)) for i in range(0, 10, 1)]
filename1 = "E:/xiaohua_pictures/"
filename2 = "E:/xiaohua_pictures2/"

def collect_datas(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text, 'lxml')
    imgs = soup.select("div.img > a > img[width=210]")

    # 将所有img的链接放在datas这个列表中
    datas = []

    # 匹配一些有问题的链接，以/d/file/开头
    pattern = re.compile("\A/d/file/")

    for img in imgs:
        data = {
            "title": img.get("alt"),
            "img": img.get("src")
        }
        match = pattern.match(data["img"])

        # 将一些有问题的地址补齐，
        if match:
            data["img"] = "http://www.xiaohuar.com" + data["img"]
        else:
            pass

        datas.append(data)

    return datas


def save_imgs(datas, filename):
    for data in datas:
        time.sleep(1)
        r = requests.get(data["img"], stream=True)
        img_name = filename + data["title"] + ".jpg"
        with open(img_name, 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)

for url in url_10:
    datas = collect_datas(url)
    print(datas)
    save_imgs(datas, filename2)
