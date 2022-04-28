
from json.tool import main
import sys
import os
import time
from selenium import webdriver
from openpyxl import Workbook
from openpyxl import load_workbook as open
from selenium.webdriver.support.ui import Select

'''
抓取所有common name
'''

if __name__ == '__main__':
    rootUrl="http://www.apc.gov.eg/en/AdvancedSearch.aspx"
    options = webdriver.ChromeOptions()
    options.add_argument("Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
    options.add_argument("Accept-Encoding=gzip, deflate")
    options.add_argument("Accept-Language=zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7")
    options.add_argument("Cache-Control=max-age=0")
    options.add_argument("Connection=keep-alive")
    options.add_argument("Cookie=ASP.NET_SessionId=nid01vgfdwufywab54woanuf; UILanguage=en-US")
    options.add_argument("Host=www.apc.gov.eg")
    options.add_argument("Upgrade-Insecure-Requests=1")
    options.add_argument("User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36")
    No_Image_loading = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", No_Image_loading)
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path="/Users/xun/Downloads/chromedriver 3",chrome_options=options)
    # 用get打开百度页面
    driver.get(rootUrl)
    driver.implicitly_wait(10)
    #设置语言
    driver.find_element_by_id("lnkBtnSwitchToArabic").click()
    driver.find_element_by_id("hlnkSwitchLanguage").click()

    commonNameSelectTag=driver.find_element_by_xpath('//*[@id="content_ContentPlaceHolder1_ddlAI"]')
    commonNameSelect = Select(commonNameSelectTag)
    for option in commonNameSelect.options:
        select_value=option.get_attribute("value")
        print(select_value+"="+option.text)
        
    driver.quit()



