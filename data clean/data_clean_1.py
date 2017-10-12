"""
from page 94
"""
import requests
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict


def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')  # 用于分割字符串
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)

    return cleanInput


def ngrams(input, n):
    input = cleanInput(input)
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output


html = requests.get("http://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(html.text, "lxml")
content = soup.find("div", {"id": "mw-content-text"}).get_text()
ngrams = ngrams(content, 2)

ngrams = OrderedDict(sorted(ngrams, key=lambda t: t[1], reverse=True))
print(ngrams)