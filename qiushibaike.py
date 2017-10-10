from bs4 import BeautifulSoup
import requests
import re

url = "https://www.qiushibaike.com/hot/page/1/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
articles = soup.select("a.contentHerf > div > span:nth-of-type(1)")

jokes = []

for article in articles:
    joke = str(article.string)
    if joke != "None":
        strinfo = re.compile("\n")
        joke = strinfo.sub('', joke)
        jokes.append(joke)

for joke in jokes:
    print(joke + "\n")
