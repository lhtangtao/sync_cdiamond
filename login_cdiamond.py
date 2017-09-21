#!/usr/bin/env python
# encoding: utf-8
"""
@author: Tangtao
@contact: tangtao@lhtangtao.com
@site: http://www.lhtangtao.com
@git:lhtangtao
@version: 
@software: PyCharm
@file: login_cdiamond.py
@time: 2017/9/21 16:32
"""
import sys
from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException

from get_conf import cdiamond_info

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


def login(infos):
    """
    传入一组信息列表 包含cdiamond的一些基础配置信息
    :param infos:
    :return:
    """
    # driver = webdriver.PhantomJS()
    driver = webdriver.Chrome()
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
    if is_element_exist(driver, '/html/body/div[2]/div/div[1]/div/ul/li[1]/h3'):
        print u'成功进入到cdiamond 配置管理中心'
    else:
        print u'没有进入到cdiamond 配置管理中心'
    driver.find_element_by_xpath('//*[@id="configId"]/a').click()
    if is_element_exist(driver, '/html/body/div[2]/div/div[2]/div/div/table/thead/tr/th[1]'):
        print u'进入到配置信息管理页面,ip为：'+infos[0]
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
    driver.find_element_by_xpath('//*[@id="queryForm"]/div/button[2]').click()  # 点击模糊查询按钮
    time.sleep(1)
    if is_element_exist(driver,'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]'):
        print u'dataid存在 下一步进行配置修改'
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td[5]/a[1]').click() # 点击编辑按钮
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="textarea"]').clear()
        driver.find_element_by_xpath('//*[@id="textarea"]').send_keys(info_to_cdiamond[2])
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="configForm"]/div[5]/button[1]').click() # 点击提交
        time.sleep(1)
        if driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]').text == u'提交成功!':
            print u'提交成功，已设置group为：'+info_to_cdiamond[0]+u' dataID为：'+info_to_cdiamond[1]+u' content为：'+ info_to_cdiamond[2]
        else:
            print u'提交失败'
    else:
        print u'dataid不存在，下一步添加配置'
if __name__ == '__main__':
    infos = cdiamond_info('test44')
    info_test = ["caocao-param", "driverWhiteSet", "111111"]
    type_infos(login(infos), info_test)
