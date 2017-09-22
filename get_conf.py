#!/usr/bin/env python
# encoding: utf-8
"""
@author: Tangtao
@contact: tangtao@lhtangtao.com
@site: http://www.lhtangtao.com
@git:lhtangtao
@version: 
@software: PyCharm
@file: get_conf.py
@time: 2017/9/21 16:04
"""
import sys
import os
import ConfigParser

reload(sys)
sys.setdefaultencoding('utf-8')


def all_cdiamond():
    """
    获取cdiamond_info.conf文件中的所有环境配置的信息
    :return:
    """
    all_cdia_info = []
    conf_path = os.path.join(os.path.dirname(__file__), 'cdiamond_info.conf')
    conf = ConfigParser.ConfigParser()
    conf.read(conf_path)
    sections = conf.sections()
    print sections
    for i in range(len(sections)):
        infos = [sections[i], conf.get(sections[i], 'address'), conf.get(sections[i], 'username'),
                 conf.get(sections[i], 'password')]
        all_cdia_info.append(infos)
    return all_cdia_info


def cdiamond_info(cdiamond_env):
    """
    输入环境名字，获取他的cdiamond地址 用户名和密码
    :return:
    """
    infos = []
    conf_path = os.path.join(os.path.dirname(__file__), 'cdiamond_info.conf')
    conf = ConfigParser.ConfigParser()
    conf.read(conf_path)
    sections = conf.sections()
    for i in range(len(sections)):
        if sections[i] == cdiamond_env:
            infos.append(conf.get(cdiamond_env, 'address'))
            infos.append(conf.get(cdiamond_env, 'username'))
            infos.append(conf.get(cdiamond_env, 'password'))
            infos.append(sections[i])
            return infos


def configure_needed():
    """
    读取configure中的所有配置信息。返回一个二维数组
    :return:
    """
    we_need = []
    conf_path = os.path.join(os.path.dirname(__file__), 'configure')
    conf = ConfigParser.ConfigParser()
    conf.read(conf_path)
    for i in range(len(conf.sections())):
        infos = [conf.get(str(i), 'group'), conf.get(str(i), 'dataId'), conf.get(str(i), 'content')]
        we_need.append(infos)
    return we_need


if __name__ == '__main__':
    # print cdiamond_info('test44')
    # print configure_needed()
    print all_cdiamond()
