import time
import os

def clock():
    while True:
        os.system('clear')  # 对于Windows, 使用 'cls'
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        time.sleep(1)

clock()
