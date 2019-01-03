import requests
from lxml import etree
import time

url = 'https://list.jd.com/list.html?cat=9987,653,655&page=1&sort=sort_totalsales15_desc&trans=1&JL=4_2_0#J_main'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}

response = requests.get(url, headers=headers)
print(response.status_code)
html = etree.HTML(response.text)

# names_list = html.xpath('//div[@class="p-price"]//i')[0].text
# for name in names_list:
# print(name.text)

# goods = html.xpath('//li[@class="gl-item"]')
# for good in goods:

ID = html.xpath(
    '//div[@class="gl-i-wrap j-sku-item"]/@data-sku_temp')

# name = html.xpath(
#     '//div[@class="p-name p-name-type3"]/a/em')
# link = good.xpath(
#     '//div[@class="p-name p-name-type3"]/a/@href').extract_first().strip()
# link2 = 'https:' + str(link)
# price = good.xpath(
#     '//div[@class="p-price"]/strong/i').extract_first().strip()
print(ID)
