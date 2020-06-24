#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/6/12 11:21
# @File    : tencen_cdn.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码
import asyncio

from app.logs import sys_log
# from app.utils.constant import MySQLStr
# from app.mydbs.database import db


# async def get_tencet_user_by_id(auth_user_id: str):
#     """根据认证ID查询用户"""
#
#     query = "".join([MySQLStr.USER_INFO, '"', auth_user_id, '"'])
#     try:
#         row = await db.fetch_one(query)
#     except Exception as e:
#         sys_log.error(msg={
#             "msg": "查询用户失败",
#             "sql": "{}".format(query),
#             "error": "{}".format(e)
#         })
#         return None
#     return row
#
#
# async def get_tencet_user_list(skip: int, limit: int):
#     """查询用户列表"""
#
#     if limit > 10000:
#         raise ValueError("最多只能查询10000条数据")
#
#     # orm的写法
#     # query = tent_users.select()
#     query = "".join([MySQLStr.USER_INFO_LIST, str(skip), ",", str(limit)])
#     try:
#         rows = await db.fetch_all(query)
#     except Exception as e:
#         sys_log.error(msg={
#             "msg": "查询用户列表失败",
#             "sql": "{}".format(query),
#             "error": "{}".format(e)
#         })
#         return None
#     return rows
#
#
# async def save_child_account_to_db(data: dict):
#     """保存腾讯子账户到数据库中"""
#
#     auth_user_id = data.get('auth_user_id')
#     if not auth_user_id:
#         raise ValueError('值错误，缺少auth_user_id')
#
#     # orm的写法
#     # query = tent_users.insert()
#     query = MySQLStr.INSERT_CHLID_ACCOUNT
#     try:
#         await db.execute(query, data)
#     except Exception as e:
#         sys_log.error(msg={
#             "msg": "保存子账户到数据库失败",
#             "sql": "{}".format(query),
#             "error": "{}".format(e)
#         })
#         return False
#     return True
#
#
# async def save_token_to_redis(token: str):
#     """将token保存到redis中"""
#
#     try:
#         await redis_session.setex(token, 7200, token)
#     except Exception as e:
#         sys_log.error(msg={
#             "msg": "保存用户的临时token到redis失败",
#             "token": "{}".format(token),
#             "error": "{}".format(e)
#         })
#         return False
#     return True
from app.models import ClientUser, ClientUserSchemaModel


async def get_tencet_user_by_id(auth_user_id: str):
    """根据认证ID查询用户"""

    try:
        user = await ClientUserSchemaModel.from_queryset_single(ClientUser.get(auth_user_id=auth_user_id))
    except Exception as e:
        sys_log.error(msg={
            "msg": "查询用户失败",
            "error": "{}".format(e)
        })
        return None
    return user


async def get_tencet_user_list(skip: int, limit: int):
    """查询用户列表"""

    if limit > 10000:
        raise ValueError("最多只能查询10000条数据")

    try:
        rows = await ClientUserSchemaModel.from_queryset(ClientUser.all().limit(limit).offset(skip))
    except Exception as e:
        sys_log.error(msg={
            "msg": "查询用户列表失败",
            "error": "{}".format(e)
        })
        return None
    return rows




