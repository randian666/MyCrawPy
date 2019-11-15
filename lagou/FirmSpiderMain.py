#!/usr/bin/env python3
import json
import time
from selenium import webdriver
from lagou import lagouMain as lg, OutputManager as out
'''
公司信息爬取
'''
class SpiderMain(object):
    def __init__(self):
        self.showId=None
        #存储到ES
        self.output=out.OutputManager()
        #lg爬取器
        self.lagou=lg.lagouMain()
    def  selenium_craw(self,page,url):
        browser.get(url)
        time.sleep(3)  # 强制等待3秒再执行下一步
        # 打印网页内容
        # html_content=browser.page_source
        print("公司信息开始处理")
        self.out_firm()
        for x in range(2, page+1):
            print("公司信息第【",x,"】页开始处理")
            #下一页
            one_page = browser.find_element_by_id("company_list").find_element_by_class_name("pager_next")
            one_page.click()
            time.sleep(1)  # 强制等待1秒再执行下一步
            self.out_firm()
            print("公司信息第【",x,"】页处理完毕")

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
if __name__ == '__main__':
    page = int(input('请输入你要抓取的页码总数：'))
    smain=SpiderMain()
    # 加载启动项
    chrome_options = webdriver.ChromeOptions()
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless') # 增加无界面选项
    chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()
    smain.selenium_craw(page,"https://www.lagou.com/gongsi/")





