import requests
kv = {"kd": "python"}
url = "http://www.baidu.com"
response = requests.get(url, params=kv)
print(response.status_code)
print(response.encoding)
print(response.text.encode("ISO-8859-1"))