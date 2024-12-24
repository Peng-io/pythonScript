import time

import psutil


def main():
    while True:
        time.sleep(1)
        cpu_liyonglv = psutil.cpu_percent()
        print("当前cpu利用率：\033[1;31;42m%s%%\033[0m" % cpu_liyonglv)


if __name__ == '__main__':
    main()
