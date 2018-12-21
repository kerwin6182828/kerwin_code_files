# -*- coding: utf-8 -*-
import scrapy
import time
import json
import re

from zufang.items import WoiwojiaItem_l1, WoiwojiaItem_l2

class WoiwojiaSpider(scrapy.Spider):
    name = 'woiwojia'
    allowed_domains = ['https://hz.5i5j.com/zufang/']
    start_urls = ['http://https://hz.5i5j.com/zufang//']


    def start_requests(self):
        print("正在写入开始时间")
        with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
            f.write("start:   " + str(time.ctime())+ "    "+str(time.time()) + "\n\n")
        base_url = "http://hz.5i5j.com/zufang/{0}/"
        districts = ["fuyangqu","xiaoshanqu",
                    ]
        # districts = ["xihuqu", "xiachengqu", "jiangganqu", "gongshuqu", "shangchengqu", "binjiangqu", "yuhangqu", "xiaoshanqu",
        #              "fuyangqu", "xiashajingjikaifaqu"]
        for district in districts:
            url_l0 = base_url.format(district)
            try:
                yield scrapy.Request(url_l0, self.parse_l0)
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")

    def parse_l0(self, response):
        house_num = int(response.css("body > div.pListBox.mar.main > div.lfBox.lf > div.total-box.noBor > span::text").extract_first())
        print(house_num)
        page_num = house_num // 30
        if house_num % 30 :
            page_num += 1
        for page in range(1, page_num+1):
            url = response.url + "o8n{0}/".format(page)
            print(url)
            try:
                yield scrapy.Request(url, self.parse_l1, dont_filter=True)
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")

    def parse_l1(self, response):
        page_block_lst = response.css("body > div.pListBox.mar.main > div.lfBox.lf > div.list-con-box > ul > li")
        for page_block in page_block_lst:
            try:
                detail_url = page_block.css("div.listCon > h3 > a::attr(href)").extract_first()
                detail_url = "https://hz.5i5j.com" + detail_url
                house_id = re.findall(r".*?zufang/(\w+).html", detail_url)[0]

                title = page_block.css("div.listCon > h3 > a::text").extract_first()
                # 三个信息连在一个标签内的，先一起爬下来，后做拆分
                span_1 = page_block.xpath("./div[2]/div[1]/p[3]/text()").extract_first()
                span_1_lst =  span_1.split("·")
                focus_num = int(re.findall("(\d+)", span_1_lst[0])[0])
                visited_num = int(re.findall("30.*?(\d+)", span_1_lst[1])[0])
                post_time = str(re.findall("(\S+)发布", span_1_lst[2])[0]).strip()

                crawl_time = time.ctime()
                crawl_time_2 = time.time()
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")


            try:
                yield scrapy.Request(detail_url, self.parse_l2, dont_filter=True)
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")

            try:
                item = WoiwojiaItem_l1()
                item["detail_url"] = detail_url
                item["house_id"] = house_id

                item["title"] = title
                item["focus_num"] = focus_num
                item["visited_num"] = visited_num
                item["post_time"] = post_time

                item["crawl_time"] = crawl_time
                item["crawl_time_2"] = crawl_time_2
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")
            yield item


    def parse_l2(self, response):
        try:
            house_id = re.findall(r".*?zufang/(\w+).html", response.url)[0]

            estate, total_floor, orientation, zone, decorate_status, building_start_year, rental_mode = ["no data" for i in range(7)]
            basic_msg_lst = response.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/ul/li")
            for basic_msg in basic_msg_lst:
                print("-------------basic_msg------------:", basic_msg)
                label = basic_msg.xpath(".//text()").extract()[0]
                value = basic_msg.xpath(".//text()").extract()[1]
                print("label:  ", label)
                print("value:  ", value)
                if "小区" in label:
                    estate = value
                elif "商圈" in label:
                    zone = value
                elif "楼层" in label:
                    total_floor = value
                elif "朝向" in label:
                    orientation = value
                elif "装修" in label:
                    decorate_status = value
                elif "年代" in label:
                    building_start_year = value
                elif "出租方式" in label:
                    rental_mode = value


            price = response.css("body > div.main.container > div.details-view.clear > div.content.fr > div.housesty > div.jlyou.fl > div > p.jlinfo::text").extract_first()
            housing_area = response.css("body > div.main.container > div.details-view.clear > div.content.fr > div.housesty > div:nth-child(3) > div > p.jlinfo::text").extract_first()
            rooms = response.css("body > div.main.container > div.details-view.clear > div.content.fr > div.housesty > div:nth-child(2) > div > p.jlinfo.font18::text").extract_first()
            district = response.css("body > div.cur-path-box > div > div > a:nth-child(5)::text").extract_first()

            agent_name = response.css("body > div.main.container > div.details-view.clear > div.content.fr > div.daikansty > ul > li.daikcon.fl > h3 > a::text").extract_first()
            agent_phone = response.css("body > div.main.container > div.details-view.clear > div.content.fr > div.daikansty > ul > li.daikcon.fl > label::text").extract_first()
            payment_method = response.xpath("/html/body/div[3]/div[2]/div[2]/div[1]/div[4]/div/p[1]/text()").extract_first()

            housing_feature, housing_introduce, nearby_supporting, decorate_description, traffic = ["no data" for i in range(5)]
            feature_lst = response.css("body > div.main.container > div.detail-main > div.box-left.fl > div:nth-child(2) > div > ul > li")
            for feature in feature_lst:
                label = feature.css("span::text").extract_first()
                value = feature.css("label::text").extract_first()
                if "亮点" in label:
                    housing_feature = value
                elif "户型" in label:
                    housing_introduce = value
                elif "配套" in label:
                    nearby_supporting = value
                elif "装修" in label:
                    decorate_description = value
                elif "交通" in label:
                    traffic = value

        except Exception as e:
            # 报错的日志输出
            with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
                f.write(str(e)+"\n\n")

        try:
            item = WoiwojiaItem_l2()
            item["house_id"] = house_id
            item["estate"] = estate
            item["price"] = price
            item["housing_area"] = housing_area
            item["rooms"] = rooms
            item["total_floor"] = total_floor
            item["orientation"] = orientation
            item["district"] = district
            item["zone"] = zone
            item["building_start_year"] = building_start_year
            item["decorate_status"] = decorate_status

            item["agent_name"] = agent_name
            item["agent_phone"] = agent_phone.strip()

            item["rental_mode"] = rental_mode
            item["payment_method"] = payment_method.strip()

            item["housing_feature"] = housing_feature
            item["housing_introduce"] = housing_introduce
            item["nearby_supporting"] = nearby_supporting
            item["nearby_supporting"] = nearby_supporting
            item["traffic"] = traffic
        except Exception as e:
            # 报错的日志输出
            with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
                f.write(str(e)+"\n\n")

        #每次yield一个item，都会经过pipeline，所以pipeline上的方法一定要多所有item都适用才行。。。
        yield item













    def parse(self, response):
        pass
