#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/5/26 16:33
# @File    : __init__.py.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码
from app.routers import cdn_views
from config import configs


def router_init(app):
    app.include_router(
        cdn_views.router,
        prefix=configs.API_V1_STR,
        tags=["Tencent_CDN"],
        # dependencies=[Depends(get_token_header)],
        responses={404: {"description": "Not found"}},
    )
