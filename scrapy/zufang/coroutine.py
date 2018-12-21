import time
def consumer():
    r = 'dick'
    while True:
        print("+++++++++++++++++++++++++++++++++++++++++++", r)
        bbb = yield r
        print("-----------------------", bbb)
        # if not bbb:
        #     return
        time.sleep(1)
        print('[CONSUMER] Consuming %s...' % bbb)
        r = '200 OK'

def produce(c):
    rr = c.send(None)
    print(">>>>>>>>>>>>>>", rr)
    print("test")
    n = 0
    while n < 5:
        n = n + 1
        time.sleep(1)
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
