from threading import Thread
from time import sleep

class ThreadTest:
    def __init__(self):
        self.num = 0

    def print_num(self):
        print("subthread start")
        while True:
            print(self.num)
            self.num += 1
            sleep(1)

print('main thread start')
th = Thread(target=ThreadTest().print_num, daemon=True)
th.start()
