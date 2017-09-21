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
            return infos

if __name__ == '__main__':
    print cdiamond_info('test44')
