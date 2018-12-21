import requests

class AbuyunProxies():

    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "H890973L0Z9I27ED"
    proxyPass = "D59ABCB3A18B8BAA"

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

# 要访问的目标页面
targetUrl = "http://test.abuyun.com"
test_ip = {"http":"http//114.237.235.225:{}"}
for i in range(3000, 20000):
    test_ip = "http//114.237.235.225:{}".format(i)
    test_ip = {"http":test_ip}

    try:
        resp = requests.get(targetUrl, proxies=test_ip)
    except Exception as e:
        print(i)
        print("wrong:   ", e)
print(i)
print(resp.status_code)
print(resp.text)
