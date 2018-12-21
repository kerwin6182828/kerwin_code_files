import pymongo
import pandas as pd
import os
import pickle
import time

import gaode

client = pymongo.MongoClient(host="localhost", port=27017)
db = client.zufang6
collection = db.lianjia

def count_estate():
    #获取杭州市所有小区的名字，通过集合去重
    """
    out : 返回一个包含所有小区名字的集合
    """
    if not os.path.exists("estate.txt"):
        print("\n读取mongo数据库数据。。。")
        total_docs = collection.find({},{"_id":0, "estate":1, "district":1})
        total_estate = set()
        for x in total_docs:
            try:
                estate = x.get("estate")
                district = x.get("district")
                total_estate.update({district+estate})
            except:
                print("wrong...")
        print(len(total_estate))
        print(total_estate)
        with open("estate.txt", "wb") as f:
            pickle.dump(total_estate, f)
    else:
        print("\n读取文本文件...")
        with open("estate.txt", "rb") as f:
            total_estate = pickle.load(f)
            print(len(total_estate))

    return total_estate


def request_gaode_all_bus(start, total_estate, is_random_proxies=True):
    #访问、计算所有小区到该小区的时间。
    # 需要用到“高德.py”那个脚本
    """
    function: 使用“高德”脚本进行请求，担心循环请求中出问题，加了一层try。（如果该轮出错，则该小区的bus时间就得不到了，略过。。。）
    out: 包含所有小区到该小区的时间的字典
    """
    bus_time_dic = {}
    count = 1
    for estate in total_estate:
        # try:
        end = estate
        d1 = gaode.crawl_1(start, is_random_proxies)
        d2 = gaode.crawl_1(end, is_random_proxies)
        # 睡一下，防止被封ip。（但是我全程同步请求，其实相当于睡好久了。。。。）
        # time.sleep(0.2)
        bus_dic = gaode.crawl_2(d1, d2, is_random_proxies)
        my_bus_dic = gaode.parse(bus_dic)
        print("\n\n")
        print(my_bus_dic)
        print("\n\n")
        bus_time_dic.update({estate:my_bus_dic["total_time"]})
        # print(bus_time_dic)
        print("           ================完成第 {0} 条数据===================".format(count))
        print(" ===========================================================================")
        print("\n\n\n\n")
        # except Exception as e:
        #     pri   nt("error:------------", e)
        # break 放在try内好像就失效了。。。现在拿出来了
        # if count == 2:
        #     break
        count += 1
    print(bus_time_dic)
    return bus_time_dic

def save_to_csv(start, bus_time_dic):
    bus_time_dic = pd.Series(bus_time_dic)
    bus_time_pd = pd.DataFrame(bus_time_dic, columns=["total_time"])
    bus_time_pd.to_csv("{}.csv".format(start), index=True, encoding="gb18030")



def main():
    # try:
    total_estate = count_estate()
    start_name = "下城区武林广场"
    bus_time_dic = request_gaode_all_bus(start_name, total_estate, is_random_proxies=False)
    save_to_csv(start_name, bus_time_dic)
    # except Exception as e:
    #     print("曹尼玛。。。。。。。。。。：", e)

if __name__ == "__main__":
    main()
