#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/6/12 10:42
# @File    : cdn_views.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码
import pickle

from fastapi import APIRouter, Depends, HTTPException

from app.utils.constant import BUSINESS, HTTP
from app.commons.tencent_cdn import account, get_child_account_token, is_tencent_child_account, get_user_resource, \
    get_auth_status
from app.commons.tencent_cdn import open_tencent_cdn
from config import configs
from app.schemas.tencten_cdn import UserListResponse, PingResponse, OpenCDNResponse, TencentLogin, PayInfoData, \
    CompanyInfoData, UserInfoData, AuthStatusResponse, UserOneResponse, TokenResponse, IKLogin, UserAuthResponse, \
    SubmitBankDataResponse, SubmitPayDataResponse, UserResourceListResponse
from app.utils.common_util import CommonQueryParams
from app.mydbs.tencen_cdn import get_tencet_user_by_id, get_tencet_user_list
from app.mydbs.database import redis_session

router = APIRouter()


@router.get("/ping", response_model=PingResponse)
async def ping():
    """
    测试模块连通性
    """
    re = {'三木': "测试redis的连接"}
    redis_session.setex("sz", 200, pickle.dumps(re))
    re_data = redis_session.get("sz")
    print(pickle.loads(re_data))
    return {'status_code': HTTP.HTTP_200_OK, "msg": "系统配置信息如下", 'data': [configs.dict()]}


