#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/6/12 12:27
# @File    : tencent_cdn.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码
import json
import pickle

from fastapi import HTTPException

from app.logs import sys_log
from app.mydbs.database import redis_session
from app.utils.constant import MyConstant, HTTP
from app.utils import tencentcloud_sdk_python as tencent
from config import configs


# CDN产品
from app.mydbs.tencen_cdn import save_child_account_to_db, get_tencet_user_by_id

production = configs.CDN_PRODUCTION_NAME

secretId = configs.TENCENT_ACCESS_ID
secretKey = configs.TENCENT_SECRET_KEY


class TencentCdnAccount(object):

    def __init__(self):
        self.secret_id = secretId
        self.secret_key = secretKey
        self.production = production

    async def make_tencent_child_account(self):
        """创建腾讯云子账户"""
        ret = await tencent.make_tencent_child_account(
            self.secret_id,
            self.secret_key
        )
        if not ret[0]:
            return False, ''
        return True, ret[1]

    async def login_tencent_cdn(self, tencent_user_id):
        """登录腾讯云获取token"""
        return await tencent.login_tencent_cdn(
            self.secret_id,
            self.secret_key,
            tencent_user_id,

        )

    async def assume_role(self, tencent_user_id):
        """获取临时秘钥"""
        return await tencent.assume_role(
            self.secret_id,
            self.secret_key,
            tencent_user_id,
        )

    async def get_auth_status(self, token):
        """获取实名状态"""

        return await tencent.get_auth_status(
            self.secret_id,
            self.secret_key,
            token
        )

    async def sumbit_bank_data(self, bank_data):
        """提交银行卡信息"""
        return await tencent.sumbit_bank_data(
            self.secret_id,
            self.secret_key,
            bank_data
        )

    async def submit_auth_code(self, pay_data):
        """提交打款信息"""
        return await tencent.submit_auth_code(
            self.secret_id,
            self.secret_key,
            pay_data
        )

    async def maker_sure_auth(self):
        """确认实名信息"""
        return await tencent.maker_sure_auth(
            self.secret_id,
            self.secret_key
        )

    async def submit_auth_info(self):
        """个人实名认证"""
        return await tencent.submit_auth_info(
            self.secret_id,
            self.secret_key
        )

    async def user_resource(self, tencent_account_id):
        """个人名下购买的资源"""
        return await tencent.user_resource(
            self.secret_id,
            self.secret_key,
            tencent_account_id
        )


account = TencentCdnAccount()


async def child_account_save_to_db(data):
    """将创建的子账号保存到数据库中"""
    ret = await save_child_account_to_db(data)
    if not ret:
        raise ValueError("保存数据失败")


async def open_tencent_cdn(tencent_account_id):
    """开通cdn"""
    return True, ''


async def get_child_assume_role_token(tencent_user_id):
    """获取腾讯子账户的临时秘钥并保存到redis中"""
    ret, token_data = await account.assume_role(tencent_user_id)
    if not ret:
        return False, ""

    try:
        redis_session.setex(tencent_user_id + "token", 7200, pickle.dumps(token_data))
        return True, token_data
    except Exception as e:
        sys_log.error(msg="保存腾讯子账号:{} token到redis失败，err：{}".format(tencent_user_id, e))
        return False, ""

"""
"tencent_user_id":{
    "expiredTime": 1506433269,
    "expiration": "2017-09-26T13:41:09Z",
    "credentials": {
        "sessionToken": "sdadffwe2323er4323423",
        "tmpSecretId": "VpxrX0IMC pHXWL0Wr3KQNCqJix1uhMqD",
        "tmpSecretKey": "VpxrX0IMC pHXWL0Wr3KQNCqJix1uhMqD"
    }
}
"""


async def get_child_account_token(tencent_user_id):
    """先去redis中拿token，没有在请求腾讯接口"""
    try:
        token_data = pickle.loads(redis_session.get(tencent_user_id + "token"))
    except Exception as e:
        token_data = None
        sys_log.error(msg="访问redis出错err:{}".format(e))

    if not token_data:
        ret, token_data = await get_child_assume_role_token(tencent_user_id)
        if not ret:
            return None
        return token_data

    return token_data


async def is_tencent_child_account(auth_user_id):
    """判断用户是否有子账户,并返回子账户ID"""

    cdn_user = await get_tencet_user_by_id(auth_user_id)
    if not cdn_user:
        raise HTTPException(
            status_code=HTTP.HTTP_404_NOT_FOUND,
        )
    if not cdn_user.tencent_user_id:
        return False, ""

    return True, cdn_user.tencent_user_id


async def get_user_resource(tencent_user_id):
    """从腾讯或者本地redis中获取用户购买的资源"""

    try:
        user_resources = pickle.loads(redis_session.get(tencent_user_id + "resources"))
    except Exception as e:
        user_resources = None
        sys_log.error(msg="访问redis出错err:{}".format(e))

    if not user_resources:
        ret, user_resources = await account.user_resource(tencent_user_id)
        if not ret:
            return None

        redis_session.setex(tencent_user_id + "resources", 7200, pickle.dumps(user_resources))

        return user_resources

    return user_resources


async def get_user_auth_info(tencent_id):
    """从腾讯获取实名信息"""
    pass


async def get_auth_status(token):
    """获取认证状态"""
    return await account.get_auth_status(token)