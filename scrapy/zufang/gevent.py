from gevent import monkey
monkey.patch_socket()
import gevent
import time

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()



for i in range(5):
    time.sleep(1)
    print(i)
