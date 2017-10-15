"""
是威廉亨利哈里森的演讲，通过演讲内容生成任意长度的马尔克夫链组成的句子
"""
import requests
from random import randint


def word_list_sum(word_list):
    sum = 0
    for word, value in word_list.items():
        sum += value
    return sum


def retrieve_random_word(word_list):
    rand_index = randint(1, word_list_sum(word_list))
    for word, value in word_list.items():
        rand_index -= value
        if rand_index <= 0:
            return word


def build_word_dict(text):
    # 剔除换行符好引号
    text = text.replace("\n", " ")
    text = text.replace("\"", "")

    # 保证每个标点符号都和前面的单词在一起
    # 这样不会被剔除， 保留在马尔克夫链中
    punctuations = [',', '.', ';', ':']
    for symbol in punctuations:
        text = text.replace(symbol, " " + symbol + " ")

    words = text.split(" ")
    # 过滤空单词
    words = [word for word in words if word != ""]
    word_dict = {}
    for i in range(1, len(words)):
        if words[i - 1] not in word_dict:
            # 为新单词创建一个词典
            word_dict[words[i - 1]] = {}
        if words[i] not in word_dict[words[i - 1]]:
            word_dict[words[i - 1]][words[i]] = 0
        word_dict[words[i - 1]][words[i]] = word_dict[words[i - 1]][words[i]] + 1

    return word_dict


url = "http://pythonscraping.com/files/inaugurationSpeech.txt"
response = requests.get(url)
word_dict = build_word_dict(response.text)

length = 100
chain = ""
current_word = "I"
for i in range(0, length):
    chain += current_word + " "
    current_word = retrieve_random_word(word_dict[current_word])

print(chain)
