data = {"string": "http://www.xiaohuar.com/d/file/ac4958d19a431bf17096323fc88e11cd.jpg"}
import requests

r = requests.get(data["string"], stream=True)
with open('E:/123.jpg', 'wb') as fd:
    for chunk in r.iter_content():
        fd.write(chunk)