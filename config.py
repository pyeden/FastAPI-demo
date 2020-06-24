#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/5/27 10:19
# @File    : config.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码
# import secrets
# secrets.token_urlsafe(128)
import io
import logging
import os
from contextlib import contextmanager
from functools import lru_cache
from io import StringIO
from typing import Optional

from dotenv.main import DotEnv
from pydantic import BaseSettings, Field


logger = logging.getLogger(__name__)


def my_get_stream(self):
    """重写python-dotenv读取文件的方法，使用utf-8，支持读取包含中文的.env配置文件"""
    if isinstance(self.dotenv_path, StringIO):
        yield self.dotenv_path
    elif os.path.isfile(self.dotenv_path):
        with io.open(self.dotenv_path, encoding='utf-8') as stream:
            yield stream
    else:
        if self.verbose:
            logger.warning("File doesn't exist %s", self.dotenv_path)
        yield StringIO('')


DotEnv._get_stream = contextmanager(my_get_stream)


class Settings(BaseSettings):
    """System configurations."""

    # 系统环境
    ENVIRONMENT: Optional[str] = Field(None, env="ENVIRONMENT")

    # 系统安全秘钥
    SECRET_KEY = 'ZEuk2U9svM2WRJql4Fs2lEvD05ZDQXZdKboim__SQqsUUqJwStZJq6u0e30bIL4Qe80PB48X1dcIZHjxqLzUiA'

    # API版本号
    API_V1_STR = "/api/v1"

    # token过期时间
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8

    # 算法
    ALGORITHM = "HS256"

    # 产品名称
    CDN_PRODUCTION_NAME = {
        "cdn": "cdn"
    }

    # 加载.env文件的配置
    class Config:
        env_file = ".env"
        case_sensitive = True


class DevConfig(Settings):
    """Development configurations."""

    # redis
    REDIS_HOST: Optional[str] = Field(None, env="DEV_REDIS_HOST")
    REDIS_PORT: Optional[int] = Field(None, env="DEV_REDIS_PORT")
    REDIS_USERNAME: Optional[str] = Field(None, env="DEV_REDIS_USERNAME")
    REDIS_PASSWORD: Optional[str] = Field(None, env="DEV_REDIS_PASSWORD")
    REDIS_DB: Optional[int] = Field(None, env="DEV_REDIS_DB")

    # 七牛玉
    QINIU_ACCESS_KEY: Optional[str] = Field(None, env="DEV_QINIU_ACCESS_KEY")
    QINIU_SECRET_KEY: Optional[str] = Field(None, env="DEV_QINIU_SECRET_KEY")
    QINIU_BUCKET_NAME: Optional[str] = Field(None, env="DEV_QINIU_BUCKET_NAME")
    QINIU_DOMAIN_NAME: Optional[str] = Field(None, env="DEV_QINIU_DOMAIN_NAME")

    # Tencent
    TENCENT_SECRET_KEY: Optional[str] = Field(None, env="DEV_TENCENT_SECRET_KEY")
    TENCENT_ACCESS_ID: Optional[str] = Field(None, env="DEV_TENCENT_ACCESS_ID")

    # Mysql
    MYSQL_SERVER: Optional[str] = Field(None, env="DEV_MYSQL_SERVER")
    MYSQL_USER: Optional[str] = Field(None, env="DEV_MYSQL_USER")
    MYSQL_PASSWORD: Optional[str] = Field(None, env="DEV_MYSQL_PASSWORD")
    MYSQL_DB_NAME: Optional[str] = Field(None, env="DEV_MYSQL_DB_NAME")
    MYSQL_PORT: Optional[int] = Field(None, env="DEV_MYSQL_PORT")


class TestConfig(Settings):
    """Production configurations."""

    REDIS_HOST: Optional[str] = Field(None, env="TEST_REDIS_HOST")
    REDIS_PORT: Optional[int] = Field(None, env="TEST_REDIS_PORT")
    REDIS_USERNAME: Optional[str] = Field(None, env="TEST_REDIS_USERNAME")
    REDIS_PASSWORD: Optional[str] = Field(None, env="TEST_REDIS_PASSWORD")
    REDIS_DB: Optional[int] = Field(None, env="TEST_REDIS_DB")

    QINIU_ACCESS_KEY: Optional[str] = Field(None, env="TEST_QINIU_ACCESS_KEY")
    QINIU_SECRET_KEY: Optional[str] = Field(None, env="TEST_QINIU_SECRET_KEY")
    QINIU_BUCKET_NAME: Optional[str] = Field(None, env="TEST_QINIU_BUCKET_NAME")
    QINIU_DOMAIN_NAME: Optional[str] = Field(None, env="TEST_QINIU_DOMAIN_NAME")

    TENCENT_SECRET_KEY: Optional[str] = Field(None, env="TEST_TENCENT_SECRET_KEY")
    TENCENT_ACCESS_ID: Optional[str] = Field(None, env="TEST_TENCENT_ACCESS_ID")

    MYSQL_SERVER: Optional[str] = Field(None, env="TEST_MYSQL_SERVER")
    MYSQL_USER: Optional[str] = Field(None, env="TEST_MYSQL_USER")
    MYSQL_PASSWORD: Optional[str] = Field(None, env="TEST_MYSQL_PASSWORD")
    MYSQL_DB_NAME: Optional[str] = Field(None, env="TEST_MYSQL_DB_NAME")
    MYSQL_PORT: Optional[int] = Field(None, env="TEST_MYSQL_PORT")


class ProdConfig(Settings):
    """Production configurations."""

    REDIS_HOST: Optional[str] = Field(None, env="PROD_REDIS_HOST")
    REDIS_PORT: Optional[int] = Field(None, env="PROD_REDIS_PORT")
    REDIS_USERNAME: Optional[str] = Field(None, env="PROD_REDIS_USERNAME")
    REDIS_PASSWORD: Optional[str] = Field(None, env="PROD_REDIS_PASSWORD")
    REDIS_DB: Optional[int] = Field(None, env="PROD_REDIS_DB")

    QINIU_ACCESS_KEY: Optional[str] = Field(None, env="PROD_QINIU_ACCESS_KEY")
    QINIU_SECRET_KEY: Optional[str] = Field(None, env="PROD_QINIU_SECRET_KEY")
    QINIU_BUCKET_NAME: Optional[str] = Field(None, env="PROD_QINIU_BUCKET_NAME")
    QINIU_DOMAIN_NAME: Optional[str] = Field(None, env="PROD_QINIU_DOMAIN_NAME")

    TENCENT_SECRET_KEY: Optional[str] = Field(None, env="PROD_TENCENT_SECRET_KEY")
    TENCENT_ACCESS_ID: Optional[str] = Field(None, env="PROD_TENCENT_ACCESS_ID")

    MYSQL_SERVER: Optional[str] = Field(None, env="PROD_MYSQL_SERVER")
    MYSQL_USER: Optional[str] = Field(None, env="PROD_MYSQL_USER")
    MYSQL_PASSWORD: Optional[str] = Field(None, env="PROD_MYSQL_PASSWORD")
    MYSQL_DB_NAME: Optional[str] = Field(None, env="PROD_MYSQL_DB_NAME")
    MYSQL_PORT: Optional[int] = Field(None, env="PROD_MYSQL_PORT")


class FactoryConfig:
    """Returns a config instance dependending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):

        if self.env_state == "development":
            return DevConfig()

        elif self.env_state == "production":
            return ProdConfig()

        elif self.env_state == "testing":
            return TestConfig()


@lru_cache()
def get_configs():
    """加载一下环境文件"""
    from dotenv import load_dotenv
    load_dotenv(encoding='utf-8')
    return FactoryConfig(Settings().ENVIRONMENT)()


configs = get_configs()











