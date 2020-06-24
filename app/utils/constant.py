#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/6/4 12:29
# @File    : constant.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码
from enum import Enum


class UserAction(str, Enum):
    """登录和注册的action参数"""
    USER_LOGIN = "login"
    USER_REGISTER = "register"


class HTTP(object):
    HTTP_100_CONTINUE = 100                            # 继续
    HTTP_101_SWITCHING_PROTOCOLS = 101                 # 交换协议
    HTTP_200_OK = 200                                  # 查询请求成功
    HTTP_201_CREATED = 201                             # 创建成功
    HTTP_202_ACCEPTED = 202                            # 接受
    HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203       # 非权威的信息
    HTTP_204_NO_CONTENT = 204                          # 没有内容
    HTTP_205_RESET_CONTENT = 205                       # 重置内容
    HTTP_206_PARTIAL_CONTENT = 206                     # 部分内容
    HTTP_207_MULTI_STATUS = 207                        # 多状态
    HTTP_300_MULTIPLE_CHOICES = 300                    # 多个选择
    HTTP_301_MOVED_PERMANENTLY = 301                   # 永久重定向
    HTTP_302_FOUND = 302                               # 发现
    HTTP_303_SEE_OTHER = 303                           # 重定向到其他
    HTTP_304_NOT_MODIFIED = 304                        # 未修改
    HTTP_305_USE_PROXY = 305                           # 使用代理
    HTTP_306_RESERVED = 306                            # 未使用
    HTTP_307_TEMPORARY_REDIRECT = 307                  # 临时重定向
    HTTP_400_BAD_REQUEST = 400                         # 错误的请求
    HTTP_401_UNAUTHORIZED = 401                        # 未经授权
    HTTP_402_PAYMENT_REQUIRED = 402                    # 需要授权
    HTTP_403_FORBIDDEN = 403                           # 禁止访问
    HTTP_404_NOT_FOUND = 404                           # 没有找到
    HTTP_405_METHOD_NOT_ALLOWED = 405                  # 方法不允许
    HTTP_406_NOT_ACCEPTABLE = 406                      # 不可接受
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407       # 代理省份验证
    HTTP_408_REQUEST_TIMEOUT = 408                     # 请求超时
    HTTP_409_CONFLICT = 409                            # 资源冲突
    HTTP_410_GONE = 410                                # 资源存在但是不可用了
    HTTP_411_LENGTH_REQUIRED = 411                     # 没有定义content-length
    HTTP_412_PRECONDITION_FAILED = 412                 # 前提条件失败
    HTTP_413_REQUEST_ENTITY_TOO_LARGE = 413            # 请求包太大
    HTTP_414_REQUEST_URI_TOO_LONG = 414                # 请求url太长
    HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415              # 不支持的媒体类型
    HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = 416     # 请求范围不足
    HTTP_417_EXPECTATION_FAILED = 417                  # 预期失败
    HTTP_422_UNPROCESSABLE_ENTITY = 422                # 不可加工
    HTTP_423_LOCKED = 423                              # 被锁定
    HTTP_424_FAILED_DEPENDENCY = 424                   # 失败的依赖
    HTTP_425_TOO_EARLY = 425                           # 言之过早
    HTTP_428_PRECONDITION_REQUIRED = 428               # 先决条件要求
    HTTP_429_TOO_MANY_REQUESTS = 429                   # 请求太多
    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431     # 请求头字段太大
    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = 451       # 由于法律原因无法使用
    HTTP_500_INTERNAL_SERVER_ERROR = 500               # 服务器错误
    HTTP_501_NOT_IMPLEMENTED = 501                     # 没有实现
    HTTP_502_BAD_GATEWAY = 502                         # 网关错误
    HTTP_503_SERVICE_UNAVAILABLE = 503                 # 服务不可用
    HTTP_504_GATEWAY_TIMEOUT = 504                     # 网关超时
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505          # HTTP协议版本不支持
    HTTP_507_INSUFFICIENT_STORAGE = 507                # 存储不足
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511     # 网络身份验证要求


class BUSINESS(object):
    # 认证相关
    INVALID_TOKEN = 20001  # 无效的token, 'Invalid token'
    ACCESS_TOKEN_EXPIRED = 20002  # access token过期, 'Access token expired'
    AUTHORIZATION_ERROR = 20004  # authorization字段错误, 'Authorization error'

    # 用户相关
    PHONE_ERROR = 20010  # 手机号格式不符合规则, 'Wrong format of mobile phone number'
    PHONE_EXISTED = 20011  # 手机号已被使用, 'Phone existed'
    EMAIL_ERROR = 20012  # 邮箱地址不符合规则, 'Wrong format of email address'
    EMAIL_EXISTED = 20013  # 邮箱地址已被使用, 'Email existed'
    PASSWORD_ERROR = 20014  # 密码不符合规则, 'Wrong format of password'
    USER_NOT_EXIST = 20016  # 账户不存在, 'Account does not exist'
    USER_OR_PASSWORD_ERROR = 20017  # 账户或密码错误, 'Wrong account or password'
    ACCOUNT_LOCKED = 20018  # 账户已被锁定, 'Account has been locked'
    ACCOUNT_EXISTED = 20019  # 账号已被使用, 'Account existed'

    # 验证码等
    CODE_ERROR = 20020  # 验证码错误, 'Wrong code'
    CODE_RESEND_ERROR = 20021  # 60s内不能重复发送验证码, '60s needed for resend'
    FILE_NOT_EXIST = 20022  # 文件不存在, 'file not found'
    EMPTY_FILE = 20023  # 文件为空, 'empty file'
    FILE_FORMAT_ERROR = 20024  # 上传的文件格式不正确, 'wrong_pic_format'

    # 腾讯cdn交互模块
    MAKE_TENT_CHILD_ACCOUNT_FIELD = 5100  # 创建用户失败
    CHILD_ACCOUNT_NOT_AUTH = 5101  # 子用户没有实名认证
    CHILD_ACCOUNT_GET_TENCENT_TOKEN_FIELD = 5102  # 获取子用户token失败
    CHILD_ACCOUNT_OPEN_CDN_FIELD = 5103  # 子用户CDN开通失败
    GET_ACCOUNT_TOKEN_FIELD = 5104  # 获取用户token失败
    GET_USER_AUTH_STATUS_FIELD = 5105  # 获取用户认证状态失败
    CDN_USER_NOT_EXISTED = 5106  # 用户不存在
    GET_ASSUME_ROLE_FIELD = 5107  # 获取用户临时秘钥失败
    CDN_API_CALL_FIELD = 5107  # API调用失败


class MyConstant(object):
    TOKEN_EXP_TIME = 8000             # 登录腾讯云数据存入redis的过期时间
    TENCENT_LOGIN = 'login'           # 登录操作


class MySQLStr(object):
    """
    sql语句
    """
    # 查询单个用户
    USER_INFO = """SELECT a.id, a.auth_user_id, a.username, a.mobile, a.real_name, a.email, a.avatar, a.status, a.tencent_user_id, a.tencent_auth_status FROM client_users AS a  WHERE a.auth_user_id = """
    # 查询用户列表
    USER_INFO_LIST = """SELECT a.id, a.auth_user_id, a.username, a.mobile, a.real_name, a.email, a.avatar, a.status, a.tencent_user_id, a.tencent_auth_status FROM client_users AS a  LIMIT """
    # 插入tencent child account
    INSERT_CHLID_ACCOUNT = """INSERT INTO client_users  (auth_user_id, tencent_user_id, tencent_auth_status) VALUES (:auth_user_id, :tencent_user_id, :tencent_auth_status)"""



