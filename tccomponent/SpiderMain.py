#!/usr/bin/env python3

from tccomponent import HtmlParser as p, OutputManager as o
from common import UrlManager as u, HtmlDownLoader as d

'''
配置中心配置列表复制粘贴到另外一个项目中
'''
class SpiderMain(object):
    def __init__(self):
        # url链接管理器
        self.urls = u.UrlManager()
        # 下载器
        self.downloader = d.HtmlDownLoader()
        # 解析器
        self.parser = p.HtmlParser()
        # 存储到ES
        self.output = o.OutputManager();
    def craw(self):
        while self.urls.has_new_url():
            print('当前未爬的url个数为：' + str(self.urls.new_url_size()))
            try:
                #获取连接
                new_url = self.urls.get_new_url()
                # 下载页面内容
                headersArgs = {
                    'Cookie': 'UM_distinctid=16a6d357ad3364-0c82210decc2fc-e323069-144000-16a6d357ad46be; _ga=GA1.2.1435867583.1555326491; access_token=507c77ae32d511f42b8984cf6c1bf3a9'}
                html_content = self.downloader.download(new_url, headersArgs=headersArgs)
                if html_content is None:
                    continue
                #解析页面内容
                jsonData = self.parser._parse_data(html_content)
                #输出内容
                if jsonData is not None and jsonData['success']:
                    self.output._add_data_to_config(jsonData['value'])
            except Exception as e:
                print("error:", e)
if __name__ == '__main__':
    spider = SpiderMain()
    spider.urls.add_new_url(
        "http://tccomponent.17usoft.com/configcenterui/getDataConfigMana?token=507c77ae32d511f42b8984cf6c1bf3a9&uk=iflight.java.dsf.itradecore&env=qa&serverRoom=Default");
    spider.craw()
