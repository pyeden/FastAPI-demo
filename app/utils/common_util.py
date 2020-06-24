#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/6/1 10:08
# @File    : common_util.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码

from datetime import datetime


class CommonQueryParams(object):
    """
    定义一个公共的查询参数类，用于fastapi的依赖
    可以以调用commons: CommonQueryParams = Depends()

    example：

        from fastapi import Depends, FastAPI

        app = FastAPI()


        fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


        class CommonQueryParams:
            def __init__(self, q: str = None, skip: int = 0, limit: int = 100):
                self.q = q
                self.skip = skip
                self.limit = limit

        @app.get("/items/")
        async def read_items(commons: CommonQueryParams = Depends()):
            response = {}
            if commons.q:
                response.update({"q": commons.q})
            items = fake_items_db[commons.skip : commons.skip + commons.limit]
            response.update({"items": items})
            return response
    """

    def __init__(self, q: str = None, skip: int = 0, limit: int = 10):
        self.q = q
        self.skip = skip
        self.limit = limit


async def write_log(api=None, msg=None, user='root'):
    with open("log.log", mode="a", encoding='utf-8') as log:
        now = datetime.now()
        log.write(f"时间：{now}    API调用事件：{api}    用户：{user}    消息：{msg}\n")
