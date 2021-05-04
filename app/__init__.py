#!/usr/bin/python
# -*- coding: utf-8 -*-

from fastapi import FastAPI

from app.middleware import middleware_init
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
    await write_log(msg='System start')


async def shutdown_event():
    await write_log(msg='System Stop')


def create_app():
    app = FastAPI(title="Sample Backend",
                  description=(
                      "API for Sample Backend."
                  ),
                  docs_url="/", )

    # 初始化日志
    log_init()

    # 加载配置
    conf_init(app)

    # 初始化中间件
    middleware_init(app)

    # 建表
    # db_init(app)

    return app
