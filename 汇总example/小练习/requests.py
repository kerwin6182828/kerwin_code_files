from pyquery import PyQuery as pq

import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
    # "Host":"hz.lianjia.com",
    "Referer" : "https://hz.lianjia.com/zufang/rs/"
}
proxies = {
    "http" :"http://localhost:1080",
    "https" :"https://localhost:1080"
}

r = requests.get("https://hz.lianjia.com/zufang/rs/", headers=headers, proxies=proxies)
# print(r.text)
with open("t1.txt", "w", encoding="utf-8") as f:
    f.write(r.text)
