from bs4 import BeautifulSoup
import requests
import time


urls = ["http://www.dianping.com/shanghai/hotel/p{}".format(i) for i in range(1,51)]

hotels_list = []

start_time = time.time()

page_number = 0

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    hotels_info = soup.select("div.hotel-info-ctn > div.hotel-info-main > h2 > a.hotel-name-link")
    for hotel_info in hotels_info:
        hotel_dic = {
            "hotel_name": hotel_info.string,
            "hotel_href": "http://www.dianping.com" + hotel_info.get("href"),
        }
        hotels_list.append(hotel_dic)
    time.sleep(1)

    page_number = page_number + 1

    print("%d of 50 pages have finished." % page_number)

end_time = time.time()
duration_time = end_time - start_time
print("you cost %.2f" % duration_time + "seconds.")
print(hotels_list)


