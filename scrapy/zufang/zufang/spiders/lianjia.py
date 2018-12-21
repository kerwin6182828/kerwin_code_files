# -*- coding: utf-8 -*-
import scrapy
import time
import json
import re
print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")

from zufang.items import LianjiaItem_l1, LianjiaItem_l2
print("D"*200)


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['hz.lianjia.com/zufang/']
    start_urls = ['http://hz.lianjia.com/zufang/rco10/']
    print("000000000000000000")


    # def start_requests(self):
    #     base_url = "http://hz.lianjia.com/zufang/{0}/rco10/"
    #     districts = ["fuyang", "xiasha"]
    #     for district in districts:
    #         url_l0 = base_url.format(district)
    #         print("11111111111111111111111111")
    #         for i in [1, 2, 3]:
    #             url = url_l0+"pg{0}/".format(i)
    #             print(time.ctime(), time.time())
    #             yield scrapy.Request(url, self.parse)



    def start_requests(self):
        print("正在写入开始时间")
        with open("bug_log_2.txt", "a", encoding="utf8") as f:
            f.write("start:   " + str(time.ctime())+ "    "+str(time.time()) + "\n\n")
        print("fucked up")
        base_url = "http://hz.lianjia.com/zufang/{0}/rco10/"
        districts = ["linan",
                    ]
        # districts = ["xihu", "xiacheng", "jianggan", "gongshu", "shangcheng", "binjiang", "yuhang", "xiaoshan",
        #             "tonglu1", "chunan1", "jiande", "fuyang", "linan", "xiasha"]
        for district in districts:
            url_l0 = base_url.format(district)
            print("11111111111111111111111111")
            # time.sleep(0.001)
            # 爬取杭州的不同区的页面
            yield scrapy.Request(url_l0, self.parse_l0)

    def parse_l0(self, response):
        print("\n\n", "^"*200)
        house_num = int(response.css("#content > div.content__article > p > span.content__title--hl::text").extract_first())
        #content > div.content__article > p > span.content__title--hl::text
        print(house_num)
        page_num = house_num // 30
        if house_num % 30 :
            page_num += 1
        for page in range(1, page_num+1):
            url = response.url + "pg{0}/".format(page)
            print(url)
            # time.sleep(0.001)
            # 爬取每个区的所有页面
            yield scrapy.Request(url, self.parse_l1, dont_filter=True)
        print("\n\n", "^"*200)

    def parse_l1(self, response):
        print("\n\n\n\n", "*"*200, "\n\n\n\n")
        print(response.status)

        page_block_lst = response.css("#content > div.content__article > div.content__list > div")
        count = 1
        for page_block in page_block_lst:
            print(count)
            count += 1


            detail_url = page_block.css("div > p.content__list--item--title.twoline > a::attr(href)").extract_first()
            detail_url = "https://hz.lianjia.com/" + detail_url

            house_id = re.findall(r".*?/(?:apartment|zufang)/(\w+).html", detail_url)[0]

            title = page_block.css("div.info-panel > h2 > a::text").extract_first()
            visited_num = page_block.css("div.info-panel > div.col-2 > div > div:nth-child(1) > span::text").extract_first()
            print(visited_num)

            building_start_year = page_block.xpath("./div[2]/div[1]/div[2]/div/text()[2]").extract_first()

            update_time = page_block.css("div.info-panel > div.col-3 > div.price-pre::text").extract_first()
            crawl_time = time.ctime()
            crawl_time_2 = time.time()

            # estate = page_block.css("div.info-panel > div.col-1 > div.where > a > span::text").extract_first()
            # rooms = page_block.css("div.info-panel > div.col-1 > div.where > span.zone > span::text").extract_first()
            # meters = page_block.css("div.info-panel > div.col-1 > div.where > span.meters::text").extract_first()
            # orientation = page_block.css("div.info-panel > div.col-1 > div.where > span:nth-child(4)::text").extract_first()
            # zone = page_block.css("div.info-panel > div.col-1 > div.other > div > a::text").extract_first()
            # total_floor = page_block.xpath("./div[2]/div[1]/div[2]/div/text()[1]").extract_first()
            # price = page_block.css("div.info-panel > div.col-3 > div.price > span::text").extract_first()

            # 测试使用
            single_house_msg = {"detail_url":detail_url, "title":title,
                                 "building_start_year":building_start_year,
            }
            print(single_house_msg)


            # 测试使用
            with open("t_l1_999.txt", "a", encoding="utf8") as f:
                f.write(str(single_house_msg)+"\n\n")

            print("just test 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            # 爬取每个区的每个页面上的每个single_block:也就是详情页
            # time.sleep(0.001)
            yield scrapy.Request(detail_url, self.parse_l2, dont_filter=True)



            item = LianjiaItem_l1()
            item["detail_url"] = detail_url
            item["house_id"] = house_id

            item["title"] = title
            item["visited_num"] = visited_num
            item["building_start_year"] = building_start_year

            item["update_time"] = update_time
            item["crawl_time"] = crawl_time
            item["crawl_time_2"] = crawl_time_2

            # item["estate"] = estate
            # item["rooms"] = rooms
            # item["meters"] = meters
            # item["orientation"] = orientation
            # item["zone"] = zone
            # item["total_floor"] = total_floor
            # item["price"] = price

            print("just test 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(item)
            yield item
        print("\n\n\n\n", "*"*200, "\n\n\n\n")





    def parse_l2(self, response):
        print("\n\n\n\n", "$"*200, "\n\n\n\n")

        house_id = re.findall(r".*?/(?:apartment|zufang)/(\w+).html", response.url)[0]
        estate = response.css("body > div:nth-child(7) > div.overview > div.content.zf-content > div.zf-room > p:nth-child(7) > a:nth-child(2)::text").extract_first()
        price = response.css("body > div:nth-child(7) > div.overview > div.content.zf-content > div.price > span.total::text").extract_first()
        housing_area = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/p[1]/text()").extract_first()
        rooms = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/p[2]/text()").extract_first()
        total_floor = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/p[3]/text()").extract_first()
        orientation = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/p[4]/text()").extract_first()
        metro = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/p[5]/text()").extract_first()
        district = response.css("body > div:nth-child(7) > div.overview > div.content.zf-content > div.zf-room > p:nth-child(8) > a:nth-child(2)::text").extract_first()
        zone = response.css("body > div:nth-child(7) > div.overview > div.content.zf-content > div.zf-room > p:nth-child(8) > a:nth-child(3)::text").extract_first()
        post_time = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/p[8]/text()").extract_first()

        agent_name = response.css("body > div:nth-child(7) > div.overview > div.content.zf-content > div.brokerInfo > div > div.brokerName > a.name.LOGCLICK::text").extract_first()
        agent_phone = response.xpath("/html/body/div[4]/div[2]/div[2]/div[3]/div/div[3]/text()").extract_first()
        agent_title = response.css("body > div:nth-child(7) > div.overview > div.content.zf-content > div.brokerInfo > div > div.brokerName > span::text").extract_first()

        rental_mode = response.xpath("//*[@id='introduction']/div/div[2]/div[1]/div[2]/ul/li[1]/text()").extract_first()
        payment_method = response.xpath("//*[@id='introduction']/div/div[2]/div[1]/div[2]/ul/li[2]/text()").extract_first()
        housing_status = response.xpath("//*[@id='introduction']/div/div[2]/div[1]/div[2]/ul/li[3]/text()").extract_first()
        heating_mode = response.xpath("//*[@id='introduction']/div/div[2]/div[1]/div[2]/ul/li[4]/text()").extract_first()

        feature_lst = response.css("#introduction > div > div.introContent > div.feature > div.featureContent > ul > li")
        for feature in feature_lst:
            print("-------------feature------------:", feature)
            label = feature.css("span.label::text").extract_first()
            value = feature.css("span.text::text").extract_first()
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


        item = LianjiaItem_l2()
        item["house_id"] = house_id
        item["estate"] = estate
        item["price"] = price
        item["housing_area"] = housing_area
        item["rooms"] = rooms
        item["total_floor"] = total_floor
        item["orientation"] = orientation
        item["metro"] = metro
        item["district"] = district
        item["zone"] = zone
        item["post_time"] = post_time

        item["agent_name"] = agent_name
        # item["agent_phone"] = agent_phone.strip()
        item["agent_title"] = agent_title

        item["rental_mode"] = rental_mode
        # item["payment_method"] = payment_method.strip()
        item["housing_status"] = housing_status
        item["heating_mode"] = heating_mode

        try:
            item["housing_feature"] = housing_feature
        except:
            print("没有这个字段啦~~~1")

        try:
            item["housing_introduce"] = housing_introduce
        except:
            print("没有这个字段啦~~~2")

        try:
            item["nearby_supporting"] = nearby_supporting
        except:
            print("没有这个字段啦~~~3")

        try:
            item["decorate_description"] = decorate_description
        except:
            print("没有这个字段啦~~~4")

        try:
            item["traffic"] = traffic
        except:
            print("没有这个字段啦~~~5")



        msg_dict = {"rooms":rooms}
        with open("t_l2_999.txt", "a", encoding="utf8") as f:
            f.write(str(msg_dict)+"\n\n")

        print("\n\n\n\n", "$"*200, "\n\n\n\n")

        yield item
        #每次yield一个item，都会经过pipeline，所以pipeline上的方法一定要多所有item都适用才行。。。
