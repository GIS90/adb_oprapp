# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 

base_info:
    __version__ = "v.10"
    __author__ = "PyGo"
    __time__ = "2021/12/27"
    __mail__ = "gaoming971366@163.com"

usage:

design:

reference urls:

python version:
    python3


Enjoy the good time everyday！！!
Life is short, I use python.

------------------------------------------------
"""
import sys
import time
import random
from operator import mod
from deploy.adb_lib import Adb2Lib
from deploy.ADB_PACKAGES import Packages as P
from deploy.utils import die
from deploy.config import DEV_IP
from deploy.logger import logger as LOG


def send_hongbao(adb, money, message, count: int = 1) -> None:
    adb.tap(1015, 1325)  # 点击+功能
    for i in range(1, 10):
        adb.tap(160, 1880)  # 红包
        adb.tap(904, 373)  # 红包金额
        adb.input(money or 0.1)  # 输入金额
        adb.tap(535, 1260)  # 塞钱进红包
        time.sleep(3)
        """开始输入密码"""
        adb.tap(540, 2140)
        adb.tap(900, 1660)
        adb.tap(540, 2140)
        adb.tap(900, 1820)
        adb.tap(180, 1660)
        adb.tap(540, 1820)
        time.sleep(3)


def send_text(adb, message, w=1) -> None:
    # adb.tap(510, 2130)
    for i in range(0, w):
        for char in message:
            adb.input(char)
        adb.tap(980, 1320)


def main():
    adb = Adb2Lib()
    is_ok, message = adb.connect(DEV_IP)
    if not is_ok: die(message)
    # if not adb.start_app(P.weixin):
    #     LOG.error('ADB start app %s failure.' % P.weixin.get('china_name'))
    # send_text(adb, message='I love you', w=3)
    send_hongbao(adb, money=0.1, message="", count=10)


if __name__ == "__main__":
    main()
    try:
        RC = 0
    except:
        RC = 1
    sys.exit(RC)
