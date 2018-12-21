import time, threading


def loop():
    print("2")
    time.sleep(5)
    print("2")

t = threading.Thread(target=loop, name='LoopThread')
t.start()
print("1")
time.sleep(8)
print("1")
t.join()
