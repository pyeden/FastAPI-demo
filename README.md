# CDN用户模块


## 简介
使用FastAPT框架构架的一个web工程，集成了数据orm工具，支持异步，拿来开箱即用的工程demo


## 技术栈

```bash
Python3.7 + FastAPI + MySQL + Redis + Tortoise-orm + aerich
```

## API接口文档地址

```bash

# host 服务器地址
http://host:8001/docs#/
http://host:8001/redoc

```

## 数据库版本管理 

```bash
# 初始化配置, 创建一个migrates文件夹和aerich.ini配置文件
aerich init -t app.mydbs.database.TORTOISE_ORM

# 数据库生成表, 并创建migrations/models迁移文件
aerich init-db 

# 新增迁移文件 *_update.json
aerich migrate

# 执行迁移文件更新数据库
aerich upgrade

# 回到上一个版本
aerich downgrade

# 查看历史迁移记录
aerich history

# 查看当前版本的迁移记录
aerich heads
```

## 目录结构说明

```bash
.
├── aerich.ini
├── app                                                       # 代码主目录
│   ├── commons                                               # 一些逻辑
│   │   ├── __init__.py 
│   │   └── tencent_cdn.py
│   ├── __init__.py
│   ├── logs                                                  # 日志配置目录
│   │   ├── __init__.py
│   ├── middleware                                            # 中间件配置目录
│   │   ├── __init__.py
│   ├── models                                                # 数据模型目录
│   │   ├── __init__.py
│   │   ├── model.py
│   ├── mydbs                                                 # 数据库相关目录
│   │   ├── database.py
│   │   ├── __init__.py
│   │   └── tencen_cdn.py
│   ├── __pycache__
│   │   └── __init__.cpython-37.pyc
│   ├── routers                                               # 路由视图目录
│   │   ├── cdn_views.py
│   │   ├── __init__.py
│   ├── schemas                                               # 参数校验模型
│   │   ├── __init__.py
│   │   └── tencten_cdn.py
│   └── utils                                                 # 工具目录
│       ├── common_util.py
│       ├── constant.py
│       ├── fake_data.py
│       ├── __init__.py
│       ├── phone_code.py
│       ├── qiniu_sdk_python.py
│       └── tencentcloud_sdk_python.py
├── config.py                                                    # 配置文件，包含生产，测试，开发三套配置
├── create_table.sql                                             # 建表sql
├── deploy.sh                                                    # docker镜像构建
├── docker-compose.yaml                                          # docker容器编排管理
├── Dockerfile                                                   # 构建镜像配置文件
├── ik_cnd_user_app_logs.log                                     # app日志
├── log.log                                                      # 日志
├── main.py                                                      # 程序启动文件
├── migrations                                                   # 数据库管理文件
│   └── models
│       ├── 0_202056062220145621_init.json
│       └── old_models.py
├── pip.conf                                                     # pip配置
├── prestart.sh                                                  # docker启动时自动执行数据库迁移脚本
├── README.md                                                    # 程序文档
├── requirements.txt                                             # 依赖环境
└── run.sh                                                       # 启动docker容器


```
