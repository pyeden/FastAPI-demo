#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/5/28 10:28
# @File    : model.py

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class MyAbstractBaseModel(Model):

    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)
    is_del = fields.IntField(null=False, default="0")

    class Meta:
        abstract = True


class ClientUser(MyAbstractBaseModel):

    auth_user_id = fields.CharField(255, null=False, unique=True)
    username = fields.CharField(100, null=True)
    mobile = fields.CharField(100, null=True)
    real_name = fields.CharField(100, null=True)
    email = fields.CharField(100, null=True)
    avatar = fields.CharField(100, null=True, default='98d2d0f6-6851-49a8-8d31-8603204cc7311591066453.png')
    status = fields.IntField(null=True)
    tencent_user_id = fields.CharField(100, null=True, unique=True)
    tencent_auth_status = fields.IntField(null=True)

    class Meta:
        table = "client_users"
        table_description = "save ik user info"
        ordering = ["-created_at", "id"]

    class PydanticMeta:
        exclude = ["created_at", "modified_at", "id"]

    def __str__(self):
        return self.auth_user_id if self.auth_user_id else "ClientUserModel"


# class TencentUser(MyAbstractBaseModel):
#     auth_user_id = fields.CharField(255, null=False, unique=True)
#     tencent_user_id = fields.CharField(100, null=True, unique=True)
#     tencent_auth_status = fields.IntField(null=True)
#
#     class Meta:
#         table = "tencent_users"
#         table_description = "save ik and tencent user info"
#         ordering = ["-created_at", "id"]
#
#     class PydanticMeta:
#         exclude = ["created_at", "modified_at", "id"]
#
#     def __str__(self):
#         return self.auth_user_id if self.auth_user_id else "UserTencentModel"


ClientUserSchemaModel = pydantic_model_creator(ClientUser, name="ClientUser")
ClientUserInSchemaModel = pydantic_model_creator(ClientUser, name="ClientUserIn", exclude_readonly=True)

# TencentUserSchemaModel = pydantic_model_creator(TencentUser, name="TencentUser")
# TencentUserInSchemaModel = pydantic_model_creator(TencentUser, name="TencentUserIn", exclude_readonly=True)
