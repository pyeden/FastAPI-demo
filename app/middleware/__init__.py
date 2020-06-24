#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/6/2 9:53
# @File    : __init__.py.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码
from starlette.middleware.cors import CORSMiddleware


# 指定允许跨域请求的url
origins = [
    "*"
]


def middleware_init(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

