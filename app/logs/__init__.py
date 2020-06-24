#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/6/11 13:23
# @File    : __init__.py.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码


import logging
from logging import handlers


sys_log = logging.getLogger('ik_cdn_user_manage')
sys_log.setLevel(level=logging.DEBUG)


def log_init():
    sys_log.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter(
        '进程ID:%(process)d - '
        '线程ID:%(thread)d- '
        '日志时间:%(asctime)s - '
        '代码路径:%(pathname)s:%(lineno)d - '
        '日志等级:%(levelname)s - '
        '日志信息:%(message)s'
    )
    sys_log.handlers.clear()
    file_handler = handlers.TimedRotatingFileHandler('ik_cnd_user_app_logs.log', encoding='utf-8', when='W6')
    file_handler.setLevel(level=logging.INFO)
    file_handler.setFormatter(formatter)
    sys_log.addHandler(file_handler)
