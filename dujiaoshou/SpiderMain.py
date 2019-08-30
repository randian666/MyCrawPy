#!/usr/bin/env python3

from dujiaoshou import HtmlParser as p,OutputManager as o
from common import UrlManager as u,HtmlDownLoader as d

class SpiderMain(object):
    def __init__(self):
        #url链接管理器
        self.urls=u.UrlManager()
        #下载器
        self.downloader=d.HtmlDownLoader()
        #解析器
        self.parser=p.HtmlParser()
        #存储到ES
        self.output=o.OutputManager();
    def craw(self):
        while self.urls.has_new_url():
            print('当前未爬的url个数为：'+str(self.urls.new_url_size()))
            try:
                new_url=self.urls.get_new_url()
                #下载页面内容
                html_content=self.downloader.download(new_url)
                if html_content is None:
                    continue
                # #解析页面内容
                new_data=self.parser._parse_data(new_url,html_content)
                # #内容存储到ES
                for json_data in new_data:
                    self.output._add_data_to_es(json_data)
            except Exception as e:
                print("error:",e)

if __name__ == '__main__':
    spider = SpiderMain()
    spider.urls.add_new_url("https://dujiaoshou.io/");
    spider.craw()




