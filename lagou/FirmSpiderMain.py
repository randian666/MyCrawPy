#!/usr/bin/env python3
import json
import time
from selenium import webdriver
from lagou import lagouMain as lg, OutputManager as out
import json

'''
公司信息爬取
'''


class SpiderMain(object):
    def __init__(self):
        self.showId = None
        # 存储到ES
        self.output = out.OutputManager()
        # lg爬取器
        self.lagou = lg.lagouMain()
        # Url集合
        self.all_urls = set()

    def selenium_crawUrl(self, url):
        browser.get(url)
        time.sleep(3)  # 强制等待3秒再执行下一步
        eles_areas = browser.find_element_by_class_name('word_list').find_elements_by_tag_name('a')
        for word in eles_areas:
            self.all_urls.add(word.get_attribute('href'))

    def craw_login(self, url):
        browser.get(url)
        time.sleep(3)  # 强制等待3秒再执行下一步

    def selenium_craw(self, page, url):
        browser.get(url)
        time.sleep(3)  # 强制等待3秒再执行下一步
        # 打印网页内容
        # html_content=browser.page_source
        print("公司信息开始处理")
        self.out_firm()
        for x in range(2, page + 1):
            print("公司信息第【", x, "】页开始处理")
            # 下一页
            one_page = browser.find_element_by_id("company_list").find_element_by_class_name("pager_next")
            one_page.click()
            time.sleep(1)  # 强制等待1秒再执行下一步
            self.out_firm()
            print("公司信息第【", x, "】页处理完毕")

    def out_firm(self):
        eles_company = browser.find_elements_by_class_name("company-item")
        for company in eles_company:
            companyid = company.get_attribute("data-companyid")
            if companyid is None:
                continue;
            companyinfo = self.lagou.get_firm(companyid)
            print(companyinfo)
            if companyinfo is None:
                continue;
            self.output._add_company_to_es(json.dumps(companyinfo))

    def loadCompanyUrl(self):
        f = open("companyurl", "r")  # 设置文件对象
        data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
        f.close()  # 关闭文件
        return data;


if __name__ == '__main__':
    smain = SpiderMain()
    # 加载启动项
    chrome_options = webdriver.ChromeOptions()
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless')  # 增加无界面选项
    chrome_options.add_argument('--disable-gpu')  # 如果不加这个选项，有时定位会出现问题
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()
    # smain.selenium_craw(20,url)
    # 获取所有地区的公司链接列表页地址
    # smain.selenium_crawUrl("https://www.lagou.com/gongsi/allCity.html?option=4-0-0-0")
    # print(smain.all_urls)
    # 分别抓取每个地区公司列表页的公司然后写入ES
    # print("当前公司列表页数量为：",len(smain.all_urls))
    urls=smain.loadCompanyUrl()
    for url in urls:
        print("开始爬取：",url)
        smain.selenium_craw(20, url)
