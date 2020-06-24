#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/6/8 10:04
# @File    : fake_data.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码
from faker import Faker


myfaker = Faker('zh_CN')


if __name__  == '__main__':
    print(myfaker.name())
    print(myfaker.address())
    print(myfaker.email())

