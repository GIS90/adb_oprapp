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
from deploy.config import DEV_IP, DEV_PORT
from deploy.logger import logger as LOG


def send_hongbao(adb, money, message, count: int = 1) -> None:
    adb.tap(1015, 2290)  # 点击+功能
    for i in range(1, 100):
        adb.tap(160, 2038)  # 红包
        adb.tap(975, 380)  # 红包金额
        adb.input(money or 0.01)  # 输入金额
        adb.tap(546, 1345)  # 塞钱进红包
        time.sleep(3)
        """开始输入密码"""
        adb.tap(540, 2270)
        adb.tap(887, 1807)
        adb.tap(540, 2270)
        adb.tap(896, 1807)
        adb.tap(182, 1821)
        adb.tap(540, 1959)
        time.sleep(3)


def send_text(adb, message, w=1) -> None:
    # adb.tap(510, 2130)
    for i in range(0, w):
        for char in message:
            adb.input(char)
        adb.tap(980, 1320)


def main():
    adb = Adb2Lib()
    DEV = '%s:%s' % (DEV_IP, DEV_PORT)
    is_ok, message = adb.connect(DEV)
    if not is_ok: die(message)
    if not adb.start_app(P.weixin):
        LOG.error('ADB start app %s failure.' % P.weixin.get('china_name'))
    # send_text(adb, message='I love you', w=3)
    send_hongbao(adb, money=0.01, message="", count=10)


if __name__ == "__main__":
    try:
        main()
        RC = 0
    except:
        RC = 1
    sys.exit(RC)
