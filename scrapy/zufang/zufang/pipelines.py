# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import re
import time

from zufang.items import LianjiaItem_l1, LianjiaItem_l2, WoiwojiaItem_l1, WoiwojiaItem_l2


class ZufangPipeline(object):
    def process_item(self, item, spider):
        return item





#处理数据格式的pipeline
class LianjiaDataProcessPipeline():
    def process_item(self, item, spider):
        # item["house_id"] = int(item["house_id"]) * 100
        print("处理中。。。。。。。。。。。。。。")
        print(item, "\n\n")

        if isinstance(item, LianjiaItem_l1):

            try:
                if "年" in item.get("building_start_year"):
                    building_start_year = re.findall(r"(\d+)年", item.get("building_start_year"))[0]
                    item["building_start_year"] = int(building_start_year)
                item["visited_num"] = int(item.get("visited_num"))
                item["update_time"] = re.findall(r"(\S+)\s", item.get("update_time"))[0]
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_2.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")

        if isinstance(item, LianjiaItem_l2):

            try:
                item["price"] = float(item.get("price"))
                item["housing_area"] = float(re.findall(r"(\S+)平", item.get("housing_area"))[0])
                item["shi"] = int(re.findall(r"(\d+)室", item.get("rooms"))[0])
                item["ting"] = int(re.findall(r"(\d+)厅", item.get("rooms"))[0])
                item["wei"] = int(re.findall(r"(\d+)卫", item.get("rooms"))[0])
                item["total_floor"] = int(re.findall(r"共(\d+)层", item.get("total_floor"))[0]) # 如果没有这个信息的话，报错怎么处理？
                post_time = int(re.findall(r"(\d+)天", item.get("post_time"))[0])
                post_time = time.asctime(time.localtime(time.time() - post_time*24*60*60))
                item["post_time"] = post_time
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_2.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")

        print(item, "\n\n")

        return item


class WoiwojiaDataProcessPipeline():
    def process_item(self, item, spider):
        print("处理中。。。。。。。。。。。。。。")

        if isinstance(item, WoiwojiaItem_l1):
            try:
                post_time = item.get("post_time")
                if "今天" in post_time:
                    post_time = time.ctime()
                elif "昨天" in post_time:
                    post_time = time.ctime()
                item["post_time"] = post_time
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")

        if isinstance(item, WoiwojiaItem_l2):
            try:
                item["price"] = float(item.get("price"))
                item["housing_area"] = float(item.get("housing_area"))
                item["total_floor"] = int(re.findall(r"/(\d+)层", item.get("total_floor"))[0])
                item["building_start_year"] = int(re.findall(r"(\d+)年", item.get("building_start_year"))[0])
                rooms = item.get("rooms")
                shi = re.findall(r"(\d+)室", rooms)[0]
                ting = re.findall(r"(\d+)厅", rooms)[0]
                item["shi"] = int(shi)
                item["ting"] = int(ting)
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")
        return item


#存储到数据库的pipeline
class MongoPipeline():

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db = crawler.settings.get("MONGO_DB")
        )

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db


    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[LianjiaItem_l1.collection_name].create_index([("house_id", pymongo.ASCENDING)])

    def process_item(self, item, spider):

        #“链家”网站的数据存储
        if isinstance(item, LianjiaItem_l1):
            print(item)
            try:
                _1 = self.db[item.collection_name].find_one({"house_id":item.get("house_id")})
                if not _1:
                    self.db[item.collection_name].insert({"house_id":item.get("house_id")})
                self.db[item.collection_name].update({"house_id":item.get("house_id")}, {"$set":dict(item)}) # 为了让item变为纯dict类型
                print("level 1...............")
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_2.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")
        if isinstance(item, LianjiaItem_l2):
            print(item)

            try:
                _1 = self.db[item.collection_name].find_one({"house_id":item.get("house_id")})
                if not _1:
                    self.db[item.collection_name].insert({"house_id":item.get("house_id")})
                self.db[item.collection_name].update({"house_id":item.get("house_id")}, {"$set":dict(item)}) # 为了让item变为纯dict类型
                print("level 2...............")

                print("存入一个完整的single房源！！！！")
                with open("bug_log_2.txt", "a", encoding="utf8") as f:
                    f.write("1个完整的房源写入成功:   " + str(time.ctime())+"    "+ str(time.time()) + "\n\n")
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_2.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")

        #“链家”网站的数据存储
        if isinstance(item, WoiwojiaItem_l1):
            try:
                _1 = self.db[item.collection_name].find_one({"house_id":item.get("house_id")})
                if not _1:
                    self.db[item.collection_name].insert({"house_id":item.get("house_id")})
                self.db[item.collection_name].update({"house_id":item.get("house_id")}, {"$set":dict(item)}) # 为了让item变为纯dict类型
                print("level 1...............")
                print(item)
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")
        if isinstance(item, WoiwojiaItem_l2):
            try:
                _1 = self.db[item.collection_name].find_one({"house_id":item.get("house_id")})
                if not _1:
                    self.db[item.collection_name].insert({"house_id":item.get("house_id")})
                self.db[item.collection_name].update({"house_id":item.get("house_id")}, {"$set":dict(item)}) # 为了让item变为纯dict类型
                print("level 2...............")
                print(item)
                print("存入一个完整的single房源！！！！")
                with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
                    f.write("1个完整的房源写入成功:   " + str(time.ctime())+"    "+ str(time.time()) + "\n\n")
            except Exception as e:
                # 报错的日志输出
                with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
                    f.write(str(e)+"\n\n")

        return item

    def close_spider(self, spider):
        print("正在写入结束时间")
        with open("bug_log_5i5j.txt", "a", encoding="utf8") as f:
            f.write("end:   " + str(time.ctime())+"    "+ str(time.time()) + "\n\n")
        self.client.close()
