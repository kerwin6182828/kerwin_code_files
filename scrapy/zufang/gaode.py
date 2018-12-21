import requests
import json
import random
import time


class AbuyunProxies():

    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "HJQKAF7YV0609R9D"
    proxyPass = "D79F76EF44F0DA9F"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }

    proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }


def my_requests(url, is_random_proxies=True):
    """
    func: 使用随机头部、随机曲奇
    """
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    ]
    print("获取随机头部")
    headers = {
        "user_agents":random.choice(user_agents),
        "Host":"www.amap.com",
    }
    dic = {}
    while True:
        try:
            t_time_1 = time.time()
            dic = requests.get(url, headers=headers)
            t_time_2 = time.time()
            print("不使用代理，访问一次的用时: ", t_time_2-t_time_1)
            dic_json = json.loads(dic.text)
            is_random_proxies = False
            if dic.status_code == 200 and dic_json.get("status")!="1":
                print("本地ip被封.....改用阿布云ip。。。")
                raise ZeroDivisionError
        except Exception as e:
            print(e)
            print("请求出错？？？改用阿布云ip。。。")
            is_random_proxies = True
            time.sleep(0.1)
        if is_random_proxies:
            print("获取随机曲奇")
            while True:
                # 每一次requests请求时候，必须记得用try，否则及其容器访问出错，或者返回的内容不是目标内容，导致后面与代码逻辑不符而报错。。。。。
                # try 搭配  for循环 !!!
                try:
                    # 对访问测时， 发现要1s左右一次。。。。。(是使用代理的缘故嘛？？)
                    t_time_1 = time.time()
                    dic = requests.get(url, headers=headers, proxies=AbuyunProxies.proxies)
                    t_time_2 = time.time()
                    print("使用阿布云代理进行一次访问的用时: ", t_time_2-t_time_1)
                except:
                    print("访问阿布云出错？？")
                    time.sleep(0.2)
                if dic:
                    break
        if dic:
            break
    return dic


# 对返回的巨型json进行解析， 提取重要的公交信息
def parse(dic):
    # 这里只挑选了第一个最佳路线
    # 总时间。总长度、总步行长度
    dic_new = {}
       # 总时间：expensetime , 总步长： allfootlength 有些json里面为空， 要不就我自己算好了，代码放下面
    try:
        total_length = int(dic.get("data").get("buslist")[0].get("allLength"))

        middle_stage = dic.get("data").get("buslist")[0].get("segmentlist") #这是一个列表
    except Exception as e:
        print("得到的dic，是非目标dic")
        print(e)
        middle_stage = []
    #预先定义好变量名，防止后面middle_stage为空时，下面变量名不会生成而在返回json时候报错
    bus_name, start_name, end_name = ["null" for i in range(3)]
    foot_time, foot_length, bus_wait_time, bus_drive_time, driver_length, this_time, this_length, this_foot_length = [0 for i in range(8)]
    # 存在距离很近不需要公交的情况：
    middle_lst = []
    total_time, total_foot_length = 0, 0
    if middle_stage:
        for i in middle_stage:
            bus_name = i.get("busname")
            start_name = i.get("startname")
            end_name = i.get("endname")

            # 走路的时间、长度
            foot_time = round(int(i.get("foottime"))/60)
            foot_length = int(i.get("footlength"))

            # 公交等待的时间， 行驶的时间
            bus_wait_time = round(int(i.get("busWaitTime", 0))/60)
            bus_drive_time = round(int(i.get("busDriveTime", 0))/60)
            driver_length = int(i.get("driverlength"))

            # 该公交的总时间、总长度、总步行长度
            this_time = foot_time + bus_wait_time + bus_drive_time
            this_length = foot_length + driver_length
            this_foot_length = foot_length
            total_time += this_time
            total_foot_length += this_foot_length
            middle_lst.append({"bus_name":bus_name, "start_name":start_name, "end_name":end_name, "foot_time":foot_time, "foot_length":foot_length,
                            "bus_wait_time":bus_wait_time, "bus_drive_time":bus_drive_time, "driver_length":driver_length,
                            "this_time":this_time, "this_length":this_length, "this_foot_length":this_foot_length,
                            })

    try:
        end_foot_time = round(int(dic.get("data").get("buslist")[0].get("endfoottime"))/60)
        end_foot_length = int(dic.get("data").get("buslist")[0].get("endfootlength"))
        total_time += end_foot_time
        total_foot_length += end_foot_length
    except Exception as e:
        print("得到的dic，是非目标dic")
        print(e)
        total_time = 99999999999
        total_length = 99999999999
        total_foot_length = 99999999999
        end_foot_time = 99999999999
        end_foot_length = 99999999999

    dic_new.update({"total_time":total_time, "total_length":total_length, "total_foot_length":total_foot_length,
                    "middle_lst":middle_lst, "end_foot_time":end_foot_time, "end_foot_length":end_foot_length,
                    })

    return dic_new


def draw(dic):
    # time
    print("\n\n时间：")
    for i in dic["middle_lst"]:
        print("-- {0} m (走)--->".format(i["foot_time"]), end=" ")
        print("-- {0} m (等)-->".format(i["bus_wait_time"]), end=" ")
        print("-- {0} m (乘)-->".format(i["bus_drive_time"]), end=" ")
    print("-- {0} m (走) ".format(dic["end_foot_time"]), end=" ")
    print("  Total Time: {0} m".format(dic["total_time"]), end=" ")


    print("\n\n公交路线: ")
    for i, j in enumerate(dic["middle_lst"]):
        print(" {0}: -->  {1}".format(i+1, j["bus_name"]))




# 获取地名相应的经纬度，以及高德内部的id
def crawl_1(keywords, is_random_proxies=True):
    url = "https://www.amap.com/service/poiTipslite?&city=330100&type=dir&words="
    url += keywords

    # 访问错误测频繁继续访问。。。
    # try:
    while True:
        res = my_requests(url, is_random_proxies)
        print(res.status_code)
        res_json = json.loads(res.text)
        if res.status_code == 200 and res_json.get("status")=="1":
            print("it's ok: ------ (crawl_1) ")
            print(url)
            break
        elif res_json.get("status")=="7":
            print("data not found", url)
            break
        else:
            print("\nit's wrong for requesting (crawl_1): sleeping...........", url, "\n\n")
            print(res_json)
            print("_________________________")
            time.sleep(0.1)

    # 如果上面json不是我想要的json，连着get会报错！！！！
    try:
        res_json = res_json.get("data").get("tip_list")[0].get("tip")
    except:
        print("res_json: ", res_json)

    name = res_json.get("name")
    district = res_json.get("district")
    x = res_json.get("x")
    y = res_json.get("y")
    id = res_json.get("poiid")
    d = {"name":name, "district":district, "x":x, "y":y, "id":id}
    print(d)
    return d
    # except Exception as e:
    #     print("wrong on [crawl_1]: ", e)
    #     return {}



# 输入起始和终点位置的经纬度坐标，会返回所有规划好的公交路线。。。（请求函数）     （接下去还要思考一下怎么分析公交路线的数据？）
def crawl_2(d1, d2, is_random_proxies=True):
    url = "https://www.amap.com/service/nav/bus?"
    params = "night=1&group=1&pure_walk=1&date=2018-12-6&time=15-30&type=0&eta=1&x1={0}&y1={1}&poiid1={2}&ad1=330103&x2={3}&y2={4}&poiid2={5}&ad2=330104"
    x1 = d1.get("x")
    y1 = d1.get("y")
    id_1 = d1.get("id")
    x2 = d2.get("x")
    y2 = d2.get("y")
    id_2 = d2.get("id")
    url = url + params.format(x1, y1, id_1, x2, y2, id_2)

    # 访问错误测频繁继续访问。。。
    # try:
    while True:
        dic = my_requests(url, is_random_proxies)
        dic_json = json.loads(dic.text)
        print(dic.status_code)
        if dic.status_code == 200 and dic_json.get("status")=="1":
            print("it's ok: ------ (crawl_2) ")
            print(url)
            break
        else:
            print("\nit's wrong for requesting (crawl_2): sleeping...........", url, "\n\n")
            time.sleep(0.1)
    return dic_json
    # except Exception as e:
    #     print("wrong on [crawl_2]: ", e)
    #     return {}

    # 返回精炼后的json
    # dic_new = parse(json.loads(dic.text))
    # 并对精炼的json进行画图————  以后如果能用matplotlib可视化可能更好些
    # draw(dic_new)



def main():
    # start = "江干区东都公寓"
    # end = "下城区仙林苑"
    start = "杭州东站"
    end = "湖滨银泰"
    d1 = crawl_1(start)
    d2 = crawl_1(end)
    bus_dic = crawl_2(d1, d2)
    my_bus_dic = parse(bus_dic)
    draw(my_bus_dic)

    # print("\n\n")
    # print(my_bus_dic.get("middle_lst")[0].get("bus_name"))

if __name__ == "__main__":
    main()
