#!/usr/bin/env python
# encoding: utf-8
"""
@author: Tangtao
@contact: tangtao@lhtangtao.com
@site: http://www.lhtangtao.com
@git:lhtangtao
@version: 
@software: PyCharm
@file: main.py
@time: 2017/9/22 10:14
"""
import sys

from get_conf import cdiamond_info, configure_needed, all_cdiamond
from selenium_cdiamond import type_infos, login

reload(sys)
sys.setdefaultencoding('utf-8')


def create_new_cdiamond(test_env):
    """
    读取configure文件中的数据，然后把里面的配置信息写入到一个环境中
    :param test_env: 环境名字 如test44 test33 test55 stable等
    :return:
    """
    infos = cdiamond_info(test_env)
    for i in range(len(configure_needed())):
        type_infos(login(infos), configure_needed()[i])


def create_all_cdiamond():
    """
    把configure里面的配置信息写到cdiamond_info.conf所提供的所有的环境
    :return:
    """
    for i in range(len(all_cdiamond())):
        create_new_cdiamond(all_cdiamond()[i][0])


if __name__ == '__main__':
    create_all_cdiamond()
    # pass