# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem_l1(scrapy.Item):
    collection_name = "lianjia"

    detail_url = scrapy.Field()
    house_id = scrapy.Field()

    title = scrapy.Field()
    visited_num = scrapy.Field()
    building_start_year = scrapy.Field()

    update_time = scrapy.Field()
    crawl_time = scrapy.Field()
    crawl_time_2 = scrapy.Field()

    # estate = scrapy.Field()
    # housing_area = scrapy.Field()
    # orientation = scrapy.Field()
    # zone = scrapy.Field()
    # total_floor = scrapy.Field()
    # price = scrapy.Field()



class LianjiaItem_l2(scrapy.Item):
    collection_name = "lianjia"

    house_id = scrapy.Field()
    estate = scrapy.Field()
    price = scrapy.Field()
    housing_area = scrapy.Field()
    rooms = scrapy.Field()
    shi = scrapy.Field()
    ting = scrapy.Field()
    wei = scrapy.Field()
    total_floor = scrapy.Field()
    orientation = scrapy.Field()
    metro = scrapy.Field()
    district = scrapy.Field()
    zone = scrapy.Field()
    post_time = scrapy.Field()

    agent_name = scrapy.Field()
    agent_phone = scrapy.Field()
    agent_title = scrapy.Field()

    rental_mode = scrapy.Field()
    payment_method = scrapy.Field()
    housing_status = scrapy.Field()
    heating_mode = scrapy.Field()

    housing_feature = scrapy.Field() # 房源亮点
    housing_introduce = scrapy.Field() # 户型介绍
    nearby_supporting = scrapy.Field() # 周边配套
    decorate_description = scrapy.Field() # 装修描述
    traffic = scrapy.Field() # 交通出行



class WoiwojiaItem_l1(scrapy.Item):
    collection_name = "woiwojia"

    detail_url = scrapy.Field()
    house_id = scrapy.Field()

    title = scrapy.Field()
    focus_num = scrapy.Field()
    visited_num = scrapy.Field()
    post_time = scrapy.Field()

    crawl_time = scrapy.Field()
    crawl_time_2 = scrapy.Field()

class WoiwojiaItem_l2(scrapy.Item):
    collection_name = "woiwojia"

    house_id = scrapy.Field()
    estate = scrapy.Field()
    price = scrapy.Field()
    housing_area = scrapy.Field()
    rooms = scrapy.Field()
    shi = scrapy.Field()
    ting = scrapy.Field()
    wei = scrapy.Field()
    total_floor = scrapy.Field()
    orientation = scrapy.Field()
    district = scrapy.Field()
    zone = scrapy.Field()
    building_start_year = scrapy.Field()
    decorate_status = scrapy.Field()

    agent_name = scrapy.Field()
    agent_phone = scrapy.Field()

    rental_mode = scrapy.Field()
    payment_method = scrapy.Field()

    housing_feature = scrapy.Field() # 房源亮点
    housing_introduce = scrapy.Field() # 户型介绍
    nearby_supporting = scrapy.Field() # 周边配套
    decorate_description = scrapy.Field() # 装修描述
    traffic = scrapy.Field() # 交通出行




class ishangzuItem_l1(scrapy.Item):
    collection_name = "ishangzu"




class qfangItem_l1(scrapy.Item):
    collection_name = "qfang"
