from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"

}

url = "https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_LIST"

wb_data = requests.get(url, headers=headers)
soup = BeautifulSoup(wb_data.text, "lxml")

imgs = soup.select('div.thumb.thumbLLR.soThumb > img')
for img in imgs:
    print(img.get('src'))