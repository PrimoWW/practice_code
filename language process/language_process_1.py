"""
from page 104
概括数据
"""
from bs4 import BeautifulSoup
import requests
import re
import string
import operator


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
    output = {}
    for i in range(len(input) - n + 1):
        ngramTemp = " ".join(input[i:i + n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output


response = requests.get("http://pythonscraping.com/files/inaugurationSpeech.txt")
ngrams = ngrams(response.text, 2)
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sortedNGrams)
