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
from selenium import webdriver
from get_conf import cdiamond_info, configure_needed, all_cdiamond, sync_cdia
from selenium_cdiamond import type_infos, login, info_from_cdia

reload(sys)
sys.setdefaultencoding('utf-8')


def create_new_cdiamond(driver, test_env):
    """
    读取configure文件中的数据，然后把里面的配置信息写入到一个环境中
    :param driver:
    :param test_env: 环境名字 如test44 test33 test55 stable等
    :return:
    """
    infos = cdiamond_info(test_env)
    for i in range(len(configure_needed())):
        type_infos(login(driver, infos), configure_needed()[i])


def create_all_cdiamond(drivers=webdriver.PhantomJS()):
    """
    把configure里面的配置信息写到cdiamond_info.conf所提供的所有的环境
    :return:
    """
    for i in range(len(all_cdiamond())):
        create_new_cdiamond(driver=drivers, test_env=all_cdiamond()[i][0])


def do_sync_cdia(drivers=webdriver.PhantomJS(), src_env="test44"):
    """
    输入源环境名称，会自动结合sync里的配置 把要同步的信息全都同步过去
    :return:
    """
    src_info = info_from_cdia(driver, src_env)
    print u"数据源为如下所示："
    print src_info
    for i in range(len(all_cdiamond())):
        env = all_cdiamond()[i][0]
        if env != src_env:
            env_infos = cdiamond_info(env)
            for z in range(len(src_info)):
                type_infos(login(driver=drivers, infos=env_infos), src_info[z])
    driver.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # create_all_cdiamond()
    do_sync_cdia(driver, 'test44')
