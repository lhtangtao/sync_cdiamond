#!/usr/bin/env python
# encoding: utf-8
"""
@author: Tangtao
@contact: tangtao@lhtangtao.com
@site: http://www.lhtangtao.com
@git:lhtangtao
@version: 
@software: PyCharm
@file: selenium_cdiamond.py
@time: 2017/9/21 16:32
"""
import sys
from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException

from get_conf import cdiamond_info, sync_cdia

reload(sys)
sys.setdefaultencoding('utf-8')
def is_element_exist(driver, xpath):
    # type: (object, object) -> object
    """
    输入xpath 判断这个元素存在与否
    :param driver:
    :param xpath:
    :return:
    """
    try:
        driver.find_element_by_xpath(xpath)
        return str(True)
    except NoSuchElementException:
        print u'元素未找到'
        return str(False)


def login(driver,infos):
    """
    传入一组信息列表 包含cdiamond的一些基础配置信息
    :param driver:
    :param infos:
    :return:
    """
    # driver = webdriver.PhantomJS()

    driver.get(infos[0])
    driver.maximize_window()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="loginForm"]/fieldset/div[1]/input').click()
    driver.find_element_by_xpath('//*[@id="loginForm"]/fieldset/div[1]/input').clear()
    driver.find_element_by_xpath('//*[@id="loginForm"]/fieldset/div[1]/input').send_keys(infos[1])
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="password"]').click()
    driver.find_element_by_xpath('//*[@id="password"]').clear()
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(infos[2])
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="loginForm"]/fieldset/button[1]').click()
    time.sleep(1)
    print '-----------------------------------------------'
    if is_element_exist(driver, '/html/body/div[2]/div/div[1]/div/ul/li[1]/h3'):
        print u'成功进入到cdiamond 配置管理中心'
    else:
        print u'没有进入到cdiamond 配置管理中心'
    driver.find_element_by_xpath('//*[@id="configId"]/a').click()
    if is_element_exist(driver, '/html/body/div[2]/div/div[2]/div/div/table/thead/tr/th[1]'):
        print u'进入环境' + infos[3] + u'到配置信息管理页面,ip为：' + infos[0]
    else:
        print u'没有进入到配置信息管理页面'
    time.sleep(1)
    return driver


def type_infos(driver, info_to_cdiamond):
    """
    把信息写入到cdiamond中去
    :param driver:
    :param info_to_cdiamond:
    :return:
    """
    driver.find_element_by_xpath('//*[@id="queryForm"]/div/input[2]').send_keys(info_to_cdiamond[1])
    driver.find_element_by_xpath('//*[@id="queryForm"]/div/input[1]').send_keys(info_to_cdiamond[0])
    driver.find_element_by_xpath('//*[@id="queryForm"]/div/button[2]').click()  # 点击模糊查询按钮
    time.sleep(1)
    len_tr = len(
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/table/tbody').find_elements_by_tag_name(
            'tr'))  # 查询得到的列表数的个数，为0则说明没有该dataid
    if len_tr != 0:
        print u'dataid存在 下一步进行配置修改'
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td[5]/a[1]').click()  # 点击编辑按钮
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="textarea"]').clear()
        driver.find_element_by_xpath('//*[@id="textarea"]').send_keys(info_to_cdiamond[2])
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="configForm"]/div[5]/button[1]').click()  # 点击提交
        time.sleep(1)
        if driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]').text == u'提交成功!':
            print u'提交成功，已设置group为：' + info_to_cdiamond[0] + u' dataID为：' + info_to_cdiamond[1] + u' content为：' + \
                  info_to_cdiamond[2]
        else:
            print u'提交失败'
    else:
        print u'dataid不存在，开始下一步添加配置'
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul[2]/button[1]').click()  # 点击添加新的配置信息按钮
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="configForm"]/div[1]/input').send_keys(info_to_cdiamond[0])
        driver.find_element_by_xpath('//*[@id="configForm"]/div[2]/input').send_keys(info_to_cdiamond[1])
        driver.find_element_by_xpath('//*[@id="textarea"]').send_keys(info_to_cdiamond[2])
        driver.find_element_by_xpath('//*[@id="configForm"]/div[5]/button[1]').click()  # 点击提交按钮
        time.sleep(1)
        if driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]').text == u'提交成功!':
            print u'提交成功，已设置group为：' + info_to_cdiamond[0] + u' dataID为：' + info_to_cdiamond[1] + u' content为：' + \
                  info_to_cdiamond[2]
        else:
            print u'提交失败'
    return driver
    # driver.quit()


def info_from_cdia(driver,src_env):
    """
    输入列表，此列表包含的信息为group 和 dataID 以及环境。 :return:一个包含所有dataid和content的二维数组 示例为：[[u'caocao-param', 'customerWhiteSet',
    u'123456'], [u'caocao-param', 'driverWhiteSet', u'123456'], [u'caocao-param', 'maxOrderBatchQuerySize', u'1']]
    """
    all_infos_sync = []
    infos = sync_cdia(src_env)
    print u"info_from_cdia函数中infos的值为："
    print infos
    for i in range(len(infos)):
        info_src = []
        driver = login(driver,cdiamond_info(src_env))
        dataid = infos[i][1]
        group = infos[i][0]
        driver.find_element_by_xpath('//*[@id="queryForm"]/div/input[1]').send_keys(group)
        driver.find_element_by_xpath('//*[@id="queryForm"]/div/input[2]').send_keys(dataid)
        driver.find_element_by_xpath('//*[@id="queryForm"]/div/button[2]').click()  # 点击模糊查询按钮
        time.sleep(1)
        content = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td[3]').text
        group = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]').text
        print u'所需要同步的数据已读取完成'
        info_src.append(group)
        info_src.append(dataid)
        info_src.append(content)
        all_infos_sync.append(info_src)
    return all_infos_sync



