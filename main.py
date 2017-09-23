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

from get_conf import cdiamond_info, configure_needed, all_cdiamond, sync_cdia
from selenium_cdiamond import type_infos, login, info_from_cdia

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


def do_sync_cdia(src_env):
    """
    把要同步的信息全都同步过去
    :return:
    """
    src_info = info_from_cdia(src_env)
    print u"数据源为如下所示："
    print src_info
    for i in range(len(all_cdiamond())):
        env = all_cdiamond()[i][0]
        if env != src_env:
            env_infos = cdiamond_info(env)
            for z in range(len(src_info)):
                type_infos(login(env_infos), src_info[z])


if __name__ == '__main__':
    do_sync_cdia('test44')
