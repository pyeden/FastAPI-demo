#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/6/12 11:03
# @File    : tencten_cdn.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码
from typing import Optional, Dict, List

from pydantic import BaseModel

from app.models import ClientUserSchemaModel


class UserStatus(BaseModel):
    status: str
    name: str


class UserInfo(ClientUserSchemaModel):
    pass


class UserResource(BaseModel):
    """用户资源"""
    id: str
    type: str
    username: str
    exp_time: str
    status: str


class TokenInfo(BaseModel):
    """腾讯子账户token信息嵌套内层"""
    sessionToken: str
    tmpSecretId: str
    tmpSecretKey: str


class TokenAllInfo(BaseModel):
    """腾讯子账户token信息嵌套外层"""
    expiredTime: str
    expiration: str
    credentials: TokenInfo


class TencentBaseResponse(BaseModel):
    """
    返回数据的基础结构
    """
    status_code: int
    msg: str


class UserListResponse(TencentBaseResponse):
    """
    返回用户列表
    """
    data: Optional[List[Optional[UserInfo]]] = None


class UserResourceListResponse(TencentBaseResponse):
    """
    返回用户资源列表
    """
    data: List[UserResource] = None


class SubmitBankDataResponse(TencentBaseResponse):
    """
    返回空
    """
    data: Dict = None


class SubmitPayDataResponse(SubmitBankDataResponse):
    """
    返回空
    """
    pass


class UserOneResponse(TencentBaseResponse):
    """
    返回一个用户
    """
    data: UserInfo = None


class TokenResponse(TencentBaseResponse):
    """
    返回子账户token
    """
    data: TokenAllInfo = None


class OpenCDNResponse(TencentBaseResponse):
    """
    开通cdn返回
    """
    data: Dict = None


class PingResponse(TencentBaseResponse):
    data: Optional[List] = None


class AuthStatusResponse(TencentBaseResponse):
    """
    返回数据的基础结构
    """
    data: UserStatus = None


class UserAuthResponse(TencentBaseResponse):
    """
    返回数据的基础结构
    """
    data: Dict = None


class UserInfoData(BaseModel):
    """
    个人实名数据结构
    """
    userIp: str
    userAgent: str
    name: str
    idcard: str
    provinceId: str
    cityId: str
    address: str


class CompanyInfoData(BaseModel):
    """
    企业实名数据结构
    """
    accountName: str
    accountId: str
    bankName: str
    bankId: str
    provinceName: str
    provinceId: str


class PayInfoData(BaseModel):
    """
    提交打款信息
    """
    authCode: str
    userIp: str
    userAgent: str


class TencentLogin(BaseModel):
    """
    登录腾讯的账户结构
    """
    tencent_account_id: str


class IKLogin(BaseModel):
    """
    登录腾讯的账户结构
    """
    auth_user_id: str
