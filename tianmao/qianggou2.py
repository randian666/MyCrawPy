#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import datetime
import time

'''
1、首先安装selenium
pip install selenium
2、下载chromedriver，要跟当前浏览器的版本一致。
https://npm.taobao.org/mirrors/chromedriver
3、把chromedriver.exe放到Anaconda3里面的Scripts中
4、运行脚本。
5、扫码登陆15秒内完成。然后输入商品抢购时间。
6、然后勾选购物车里面想要抢购的商品
7、返回程序，在控制台中输入2代表手动勾选商品抢购
'''
def login():
    # 打开淘宝登录页，并进行扫码登录
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)

    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(times, choose):
    is_buyed = False
    # 点击购物车里全选按钮
    if choose == 2:
        print("请手动勾选需要购买的商品")
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print('现在时间：', now)
        # 对比时间，时间到的话就点击结算
        if now > times:
            if choose == 1:
                while True:
                    try:
                        if browser.find_element_by_id("J_SelectAllcbx1"):
                            browser.find_element_by_id("J_SelectAllcbx1").click()
                            print('尝试全选')
                            break
                    except:
                        print("找不到全选按钮")
            # 点击结算按钮
            try:
                if browser.find_element_by_id("J_Go"):
                    browser.find_element_by_id("J_Go").click()
                    print("结算成功")
            except:
                pass
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单') and is_buyed == False:
                        browser.find_element_by_link_text('提交订单').click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("抢购成功时间：%s" % now1)
                except:
                    print("再次尝试提交订单")
            time.sleep(0.005)

if __name__ == "__main__":
    times = input("请输入抢购时间，格式如(2019-11-11 16:00:00.000000):")
    browser = webdriver.Chrome()
    browser.maximize_window()
    login()
    choose = input("到时间自动勾选购物车请输入“1”，否则输入“2”：")
    buy(times, choose)