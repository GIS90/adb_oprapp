# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 

base_info:
    __author__ = "PyGo"
    __time__ = "2024/5/8 12:47"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "adb_oprapp"

usage:

design:

reference urls:

python version:
    python3


Enjoy the good life everyday！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python weixinyuedu.py
# ------------------------------------------------------------
import subprocess
import random
import time
import datetime


CMD1 = 'which /usr/local/bin/adb'
# start_x, start_y, end_x, end_y, timer=150
CMD2 = '/usr/local/bin/adb -s 192.168.101.9:5555 shell input swipe 750 1000 450 1000 200'


def run_cmd_1(cmd_string):
    # print('运行cmd指令：{}'.format(cmd_string))
    result = subprocess.run(cmd_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # 打印命令的输出和错误信息
    # print(result.stdout, result.stderr)
    return result


def main():
    for i in range(1, 9999):
        sleep_time = round(random.uniform(12.5, 20.5), 2)
        print("执行点击翻页【%s】次，翻页间隔时间：%s，当前时间：%s" % (i, sleep_time, datetime.datetime.now()))
        time.sleep(sleep_time)
        run_cmd_1(CMD2)


if __name__ == "__main__":
    main()

