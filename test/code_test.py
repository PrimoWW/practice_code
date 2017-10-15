"""
just a file that i can test some short codes here
"""
import requests
params={"username": "primo", "password": "password"}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print("------------------")
print("Goinng to profile page...")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)