#!/usr/bin/env python3

from star import UrlManager as u,HtmlDownLoader as d,HtmlParser as p,OutputManager as o
class SpiderMain(object):
    def __init__(self):
        #url链接管理器
        self.urls=u.UrlManager()
        #下载器
        self.downloader=d.HtmlDownLoader()
        #解析器
        self.parser=p.HtmlParser()
        #存储器
        self.output=o.OutputManager();
    def craw_root(self,root_url):
        # 下载根页面内容
        html_content = self.downloader.download(root_url)
        new_urls=self.parser._parse_url(root_url,html_content)
        #把根页面的链接放入链接管理器
        self.urls.add_new_urls(new_urls)
    def craw(self):
        while self.urls.has_new_url():
            try:
                #从url管理器中获取一个链接
                new_url=self.urls.get_new_url()
                #下载页面内容
                html_content=self.downloader.download(new_url)
                #解析页面内容
                new_urls,new_data=self.parser.parse(new_url,html_content)
                #当前页面抓取到的链接
                self.urls.add_new_urls(new_urls)
                #内容存储到ES
                self.output._add_data_to_es(new_data)
            except Exception as e:
                print("error:",e)

if __name__ == '__main__':
    spider = SpiderMain()
    #解析根页面获取链接地址
    spider.craw_root("http://v.qq.com/x/star/80597&tabid=2")
    #解析页面写入ES并获取链接写入redis
    spider.craw()


