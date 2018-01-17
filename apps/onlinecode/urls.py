#! usr/bin/python
#coding=utf-8

'''
模块名称：
模块主要功能：
模块实现的方法：
模块对外接口：
模块作者：
编写时间：
修改说明：
修改时间：
'''

'''
功能：在线练习的路由
创建时间：2017.10.26
最后修改时间：2017.10.26
'''

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^online_practice/', OnlinePractice.as_view(), name='onlinepractice'),
]