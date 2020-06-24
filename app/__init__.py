#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/5/26 16:27
# @File    : __init__.py.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码


from fastapi import FastAPI

from app.middleware import middleware_init
from app.routers import router_init
from app.logs import log_init, sys_log
from app.mydbs.database import db_init
from app.utils.common_util import write_log


def conf_init(app):
    from config import configs
    sys_log.info(msg=f'Start app with {configs.ENVIRONMENT} environment')
    if configs.ENVIRONMENT == 'production':
        app.docs_url = None
        app.redoc_url = None
        app.debug = False


async def start_event():
    await write_log(msg='系统启动')


async def shutdown_event():
    await write_log(msg='系统关闭')


def create_app():
    app = FastAPI(title="CDN_USER_API",
                  description="cnd平台用户模块接口文档",
                  version="1.0.0",
                  on_startup=[start_event],
                  on_shutdown=[shutdown_event]
                  )

    # 初始化日志
    log_init()

    # 加载配置
    conf_init(app)

    # 初始化路由配置
    router_init(app)

    # 初始化中间件
    middleware_init(app)

    # 建表
    db_init(app)

    return app
