import requests
import json
import re


url = "http://pic.haibao.com/ajax/image:getHotImageList.json?stamp=Thu%20Dec%2013%202018%2003%3A08%3A56%20GMT%200800%20%28%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4%29"
url = "http://pic.haibao.com/ajax/image:getHotImageList.json?stamp=Thu%20Dec%2013%202018%2003%3A08%3A56%20GMT%200800%20%28%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4%29"
url = "http://pic.haibao.com/ajax/image:getHotImageList.json?stamp=Thu%20Dec%2013%202018%2003%3A08%3A56%20GMT%200800%20%28%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4%29"

headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
        "Host":"pic.haibao.com"
}


ids_lst_all = []
skip = 0
while True:
    data = {"skip":skip}
    r = requests.post(url, headers=headers, data=data)
    r = r.text[-1000:-1]
    ids = re.findall('"ids":"(.*?)"', r)[0]
    skip = int(re.findall('"skip":(\d+)', r)[0])
    ids_lst_batch = ids.split(",")
    ids_lst_all.extend(ids_lst_batch)
    if skip == 1000:
        break

url_lst_all = ["http://pic.haibao.com/image/{0}.html".format(ids) for ids in ids_lst_all]
with open("total_urls.txt", "w", encoding="utf-8") as f:
    for url in url_lst_all:
        f.write(url+"\n\n")

print("The number of total urls:  ", len(set(url_lst_all)))
