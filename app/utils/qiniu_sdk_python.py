#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/5/27 9:35
# @File    : qiniu-sdk-python.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码
import time
import uuid

from qiniu import Auth, put_file
# from app.databases.database import get_db

from config import configs


img_suffix = ["jpg", "png"]


def upload_data_to_qiniu(file_data):
    """
    # 数据上传七牛云对象存储
    """
    q = get_auth_object()

    save_name = file_check(file_data)

    token = generate_upload_token(q, save_name)

    try:
        ret, info = upload_file(token, save_name, file_data)
        if info.status_code == 200:
            key = ret.get("key")
            return True, key
        else:
            return False, '文件上传七牛云失败'
    except:
        return False, '文件上传七牛云失败'


def generate_upload_token(auth_object, save_name):
    """
    :param auth_object: 鉴权对象
    :return: 上传token
    """
    # 生成上传 Token，可以指定过期时间等
    return auth_object.upload_token(configs.QINIU_BUCKET_NAME, save_name, 3600)


def get_auth_object():
    """
    :return: 鉴权对象
    """
    # 构建鉴权对象
    return Auth(configs.QINIU_ACCESS_KEY, configs.QINIU_SECRET_KEY)


def file_check(file_data):
    """
    :param file_data:传入的文件名
    :return:
    """
    # 上传后保存的文件名
    file_str_list = file_data.split('.')
    if file_str_list[1] not in img_suffix:
        raise ValueError('请上传文件后缀为"jpg", "png"的头像文件')
    save_file_name = make_save_name()
    return save_file_name


def make_save_name():
    return ''.join([str(uuid.uuid4()), str(time.time()).split('.')[0], '.', 'png'])


def upload_file(token, key, file_data):
    """
    :param token: 上传token
    :param key: 上传后保存的文件名
    :param file_data: 上传的文件
    :return:
    """
    return put_file(token, key, file_data)


def private_download_url(key):
    q = get_auth_object()
    base_url = ''.join([configs.QINIU_DOMAIN_NAME, key])
    return q.private_download_url(base_url, expires=3600)


def save_key_db(key):
    # db_session = get_db
    pass


if __name__ == "__main__":
    file = 'C:/Users/IK/Desktop/senzhong.jpg'
    # settings = type('settings', (object,), dict(
    #     QINIU_DOMAIN_NAME='http://qayumwil2.bkt.clouddn.com/',
    #     QINIU_ACCESS_KEY='QMZp9UCZ0VhdcAS6R0RvWMT9cTI3vwOH2h13Qm47',
    #     QINIU_SECRET_KEY='34iPk_IX6bE0mhabY-TSp-6eDBu3akj196PMo28D',
    #     QINIU_BUCKET_NAME='dengsz'
    # ))
    res = upload_data_to_qiniu(file)
    print(res)
    print(private_download_url(res[1]))
    # print(private_download_url('f54ad132-5e27-447d-8018-0bea375496931591067315.png'))
    # import pymysql
    # pymysql.install_as_MySQLdb()
    # engine = create_engine("mysql://root:123456@localhost:3306/users?charset=utf8", pool_size=20, max_overflow=0)
    #
    # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # db = SessionLocal()
    # obj_in = {
    #     'phone': 180114111066,
    #     'email': '1011@qq.com',
    #     'hashed_password': '1213456',
    #     'head_image_url': 'bc3b6db0-7e61-4505-ac2f-53e1e651467d1590629068.png'
    # }
    # CRUDUser(User).create(db, obj_in=obj_in)
    # save_key_db('f54ad132-5e27-447d-8018-0bea375496931591067315.png')

    # http://qayumwil2.bkt.clouddn.com/bc3b6db0-7e61-4505-ac2f-53e1e651467d1590629068.png
    pass
