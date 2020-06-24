#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/5/28 10:03
# @File    : database.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码


import redis
from tortoise.contrib.fastapi import register_tortoise

from config import configs


# mysql数据库url
SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}:{}/{}?charset=utf8".format(
    configs.MYSQL_USER,
    configs.MYSQL_PASSWORD,
    configs.MYSQL_SERVER,
    configs.MYSQL_PORT,
    configs.MYSQL_DB_NAME
)

# 数据库迁移配置
TORTOISE_ORM = {
    "connections": {"default": SQLALCHEMY_DATABASE_URL},
    "apps": {
        "models": {
            "models": ["aerich.models", "app.models.model"],
            # 须添加“aerich.models” 后者“models”是上述models.py文件的路径
            "default_connection": "default",
        },
    },
}


# db = databases.Database(SQLALCHEMY_DATABASE_URL)
# metadata = sqlalchemy.MetaData()
# engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL, pool_size=20, max_overflow=0, echo=True)
# metadata.create_all(engine)


def db_init(app):
    register_tortoise(
        app,
        db_url=SQLALCHEMY_DATABASE_URL,
        modules={"models": ["app.models.model"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )


# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# class CustomBase(object):
#
#     @declared_attr
#     def __tablename__(cls):
#         return cls.__name__.lower()
#
#
# async def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# Base = declarative_base(cls=CustomBase)


pool = redis.ConnectionPool(
    host=configs.REDIS_HOST,
    port=configs.REDIS_PORT,
    # password=configs.REDIS_PASSWORD,
    db=configs.REDIS_DB,
)
redis_session = redis.Redis(connection_pool=pool)


if __name__ == "__main__":
    token = {
        "expiredTime": "1506433269",
        "expiration": "2017-09-26T13:41:09Z",
        "credentials": {
            "sessionToken": "sdadffwe2323er4323423",
            "tmpSecretId": "VpxrX0IMC pHXWL0Wr3KQNCqJix1uhMqD",
            "tmpSecretKey": "VpxrX0IMC pHXWL0Wr3KQNCqJix1uhMqD"
        }
    }

    import pickle
    redis_session.setex("user", 100, pickle.dumps(token))
    print(pickle.loads(redis_session.get("user")))

