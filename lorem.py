import platform
import random
import time
import os
val = 0.256
x = 0
deadx = 0
os.system("clear")
os.getlogin()
while True:
    x += 1
    deadx -= 1
    print(f"m\033[94m{platform.platform()}- 3 ---        | Ipsum")
    time.sleep(val)
    print(f"\033[92m{platform.platform()}-- . ---        | Lorem")
    time.sleep(val)
    print(f"\033[93m{platform.platform()}--- 1 ---------------- {deadx}  \033[32mą, ć, ę, ł, ń, ó, ś, ź, ż")
    time.sleep(val)
    print(f"\033[91m{platform.platform()}---- 4 ---------------- {x}  \033[32m愛 時 愛 時")
    time.sleep(val)
    print(f"\033[90m{platform.platform()}-----{os.getlogin()} 3.1415926535897932384626433832795028841971693993751058209749 --- !@#$%^&*()-=+\|]][]")
    time.sleep(val)