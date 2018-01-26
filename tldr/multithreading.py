import threading
import time

def worker(name):
    print(name)
    print(time.time())

a = threading.Thread(target=worker("A"))
b = threading.Thread(target=worker("B"))
a.start()
b.start()
a.join()
b.join()
