#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/5/26 17:09
# @File    : tencentcloud-sdk-python.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

from app.logs import sys_log


async def make_tencent_child_account(secret_id, secret_key):
    """
    创建腾讯云子账户
    可以重复调用，不会再次注册，会返回已经注册的用户
    {
        "qcloudUin" 1003121321,
        "qcloudAppid" 132332323
    }
    """
    # 导入对应产品模块的 client models。
    from tencentcloud.partners.v20180321 import partners_client, models

    try:
        cred = credential.Credential(secret_id, secret_key)
        client = partners_client.PartnersClient(cred, production)
        req = models.DescribeZonesRequest()
        resp = client.DescribeZones(req)

        json_data = resp.to_json_string()
        if json_data.get("code") == 0:
            return True, json_data.get("data")
        else:
            sys_log.error(msg="腾讯云API内部处理错误，请联系腾讯工程师，api：ChannelRegisterUser，err={}"
                          .format(json_data.get("message")))
            return False, ""
    except TencentCloudSDKException as err:
        sys_log.error(msg="调用腾讯云CDN业务API失败，err={}".format(err))
        return False, ""


async def login_tencent_cdn(secret_id, secret_key, tencent_user_id):
    """
    渠道侧获取用户登录控制台所需 token
    注1：token有效期为5分钟。
    注2：得到token之后，拼接url地址：
    https://cloud.tencent.com/login/channelAccessCallback?fromUin=1234567
    &token=Zx7Ut1m3181lCm26uko579OE24BTtY1d&signature=seJLwb6RxVj9q3OK8ezE9UoFqSQ%3D
    &redirect_uri=https%3A%2F%2Fconsol e.cloud.tencent.com%2F
    用户跳转至该连接即可下发登录态并且跳转至指定url.其中参数：token 为上文接
    口获得返回值， uin 为渠道侧主 uin,$key 为上文接口获得返回值 key 。签名方法为：
    php
    签名代码：
    $signature = urlencode(base64_encode(hash_hmac('sha1', $token.$uin, $key,
    true)));

    {
        "token": xadadad,
        "key": xadadad,
        "expiredTime": 1506433269
    }

    """

    try:
        cred = credential.Credential(secret_id, secret_key)
        client = cdn_client.CdnClient(cred, production)
        req = models.DescribeZonesRequest()
        resp = client.DescribeZones(req)

        json_data = resp.to_json_string()
        if json_data.get("code") == 0:
            return True, json_data.get("data")
        else:
            sys_log.error(msg="腾讯云API内部处理错误，请联系腾讯工程师，api：ChannelGetLogin Token，err={}"
                          .format(json_data.get("message")))
            return False, ""
    except TencentCloudSDKException as err:
        sys_log.error(msg="调用腾讯云CDN业务API失败，err={}".format(err))
        return False, ""


async def assume_role(secret_id, secret_key, tencent_user_id):
    """
    获取临时秘钥
    {
        "expiredTime": 1506433269,
        "expiration": "2017-09-26T13:41:09Z",
        "credentials": {
            "sessionToken": "sdadffwe2323er4323423",
            "tmpSecretId": "VpxrX0IMC pHXWL0Wr3KQNCqJix1uhMqD",
            "tmpSecretKey": "VpxrX0IMC pHXWL0Wr3KQNCqJix1uhMqD"
    }
    """

    try:
        cred = credential.Credential(secret_id, secret_key)
        client = cdn_client.CdnClient(cred, production)
        req = models.DescribeZonesRequest()
        resp = client.DescribeZones(req)

        json_data = resp.to_json_string()
        if json_data.get("code") == 0:
            return True, json_data.get("data")
        else:
            sys_log.error(msg="腾讯云API内部处理错误，请联系腾讯工程师，api：AssumeRole Token，err={}"
                          .format(json_data.get("message")))
            return False, ""
    except TencentCloudSDKException as err:
        sys_log.error(msg="调用腾讯云CDN业务API失败，err={}".format(err))
        return False, ""


async def get_auth_status(secret_id, secret_key, token):
    """
    获取实名状态
    status 状态含义：
    0 未实名
    1 未实名，打款中（提交银行卡信息后即为此状态）（只有企业实名会有这
    个状态，个人实名不会出现）
    2 未实名，银行卡信息不正确（只有企业实名会有这个状态，个人实名不
    会出现）
    33 : 用户输入打款金额并且正确后，待确认。确认后即完成实名，变为状态 3
    （只有企业实名会有这个状态，个人实名不会出现
    3 已经完成实名。此时 name 表示实名信息

    {"status": "3","name": "dad_dwd"}
    """

    try:
        cred = credential.Credential(secret_id, secret_key)
        client = cdn_client.CdnClient(cred, production)
        req = models.DescribeZonesRequest()
        resp = client.DescribeZones(req)

        json_data = resp.to_json_string()
        if json_data.get("code") == 0:
            return True, json_data.get("data")
        else:
            sys_log.error(msg="腾讯云API内部处理错误，请联系腾讯工程师，api：GetAuthStatus Token，err={}"
                          .format(json_data.get("message")))
            return False, ""
    except TencentCloudSDKException as err:
        sys_log.error(msg="调用腾讯云CDN业务API失败，err={}".format(err))
        return False, ""


async def sumbit_bank_data(secret_id, secret_key, bank_data):
    """
    提交银行卡信息
    {}
    """

    try:
        cred = credential.Credential(secret_id, secret_key)
        client = cdn_client.CdnClient(cred, production)
        req = models.DescribeZonesRequest()
        resp = client.DescribeZones(req)

        json_data = resp.to_json_string()
        if json_data.get("code") == 0:
            return True, json_data.get("data")
        else:
            sys_log.error(msg="腾讯云API内部处理错误，请联系腾讯工程师，api：SubmitBankData Token，err={}"
                          .format(json_data.get("message")))
            return False, ""
    except TencentCloudSDKException as err:
        sys_log.error(msg="调用腾讯云CDN业务API失败，err={}".format(err))
        return False, ""


async def submit_auth_code(secret_id, secret_key, pay_data):
    """
    提交打款信息
    {}
    """

    try:
        cred = credential.Credential(secret_id, secret_key)
        client = cdn_client.CdnClient(cred, production)
        req = models.DescribeZonesRequest()
        resp = client.DescribeZones(req)

        json_data = resp.to_json_string()
        if json_data.get("code") == 0:
            return True, json_data.get("data")
        else:
            sys_log.error(msg="腾讯云API内部处理错误，请联系腾讯工程师，api：SubmitAuthCode Token，err={}"
                          .format(json_data.get("message")))
            return False, ""
    except TencentCloudSDKException as err:
        sys_log.error(msg="调用腾讯云CDN业务API失败，err={}".format(err))
        return False, ""


async def maker_sure_auth(secret_id, secret_key):
    """
    确认实名信息
    实名认证步骤：
        1.未提交实名信息时，用户 认证状态为 0
        2.提交银行卡信息，此时用户实名认证状态为 1
        3.用户收到打款后，提交打款正确信息，此时状态为 33 。如果用户信息错误，状态为 2 。
        4.用户确认实名认证信息，调用确认接口。确认后用户实名状态为 3.
        5.用户重新提交银行卡相关信息，此时用户实名状态又变成 1 。
        6.每一个状态均可以通过查询接口查询获取。
    {}
    """

    try:
        cred = credential.Credential(secret_id, secret_key)
        client = cdn_client.CdnClient(cred, production)
        req = models.DescribeZonesRequest()
        resp = client.DescribeZones(req)

        json_data = resp.to_json_string()
        if json_data.get("code") == 0:
            return True, json_data.get("data")
        else:
            sys_log.error(msg="腾讯云API内部处理错误，请联系腾讯工程师，api：MakeSureAuth Token，err={}"
                          .format(json_data.get("message")))
            return False, ""
    except TencentCloudSDKException as err:
        sys_log.error(msg="调用腾讯云CDN业务API失败，err={}".format(err))
        return False, ""


async def submit_auth_info(secret_id, secret_key):
    """
    个人实名认证
    如果用户没有财付通绑过卡，会返回qid和qurl ，
    根据qurl生成二维码进行展示。用户会使用微信扫描二维码进行支付，
    支付通过后会通过认证，此时调用实名状态查询接口会返回已经通过实名认证。

    {
        "qurl": "weixin://xxx/xx"   # 如果曾经财付通绑过卡，会直接通过， data 为空
        "qid": "dadadasd"
    }
    """

    try:
        cred = credential.Credential(secret_id, secret_key)
        client = cdn_client.CdnClient(cred, production)
        req = models.DescribeZonesRequest()
        resp = client.DescribeZones(req)

        json_data = resp.to_json_string()
        if json_data.get("code") == 0:
            return True, json_data.get("data")
        else:
            sys_log.error(msg="腾讯云API内部处理错误，请联系腾讯工程师，api：SubmitAuthInfo Token，err={}"
                          .format(json_data.get("message")))
            return False, ""
    except TencentCloudSDKException as err:
        sys_log.error(msg="调用腾讯云CDN业务API失败，err={}".format(err))
        return False, ""


async def user_resource(secret_id, secret_key, tencent_account_id):
    """
    个人名下购买的资源

    [
        {
            "id": "资源id"，
            "type": "资源类型",
            "username": "用户名",
            "exp_time": "到期时间"，
            "status": "状态"
        }
    ]
    """

    try:
        cred = credential.Credential(secret_id, secret_key)
        client = cdn_client.CdnClient(cred, production)
        req = models.DescribeZonesRequest()
        resp = client.DescribeZones(req)

        json_data = resp.to_json_string()
        if json_data.get("code") == 0:
            return True, json_data.get("data")
        else:
            sys_log.error(msg="腾讯云API内部处理错误，请联系腾讯工程师，api：SubmitAuthInfo Token，err={}"
                          .format(json_data.get("message")))
            return False, ""
    except TencentCloudSDKException as err:
        sys_log.error(msg="调用腾讯云CDN业务API失败，err={}".format(err))
        return False, ""


if __name__ == "__main__":
    pass
    """
    {
      "TotalCount": 7,
      "ZoneSet": [
        {
          "Zone": "ap-shanghai-1",
          "ZoneName": "上海一区",
          "ZoneId": "200001",
          "ZoneState": "UNAVAILABLE"
        },
        {
          "Zone": "ap-shanghai-2",
          "ZoneName": "上海二区",
          "ZoneId": "200002",
          "ZoneState": "AVAILABLE"
        },
        {
          "Zone": "ap-shanghai-3",
          "ZoneName": "上海三区",
          "ZoneId": "200003",
          "ZoneState": "AVAILABLE"
        },
        {
          "Zone": "ap-shanghai-4",
          "ZoneName": "上海四区",
          "ZoneId": "200004",
          "ZoneState": "AVAILABLE"
        },
        {
          "Zone": "ap-shanghai-5",
          "ZoneName": "上海五区",
          "ZoneId": "200005",
          "ZoneState": "UNAVAILABLE"
        },
        {
          "Zone": "ap-shanghai-6",
          "ZoneName": "上海六区",
          "ZoneId": "200006",
          "ZoneState": "UNAVAILABLE"
        },
        {
          "Zone": "ap-shanghai-7",
          "ZoneName": "上海七区",
          "ZoneId": "200007",
          "ZoneState": "UNAVAILABLE"
        }
      ],
      "RequestId": "ddd01d85-b23b-4d75-be96-ad07e32fdfc0"
    }
    
    """
