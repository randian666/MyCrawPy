#!/usr/bin/env python3

from boss import UrlManager as u,HtmlDownLoader as d,HtmlParser as p,OutputManager as o
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
    def craw_root(self,root_url):
        # 下载根页面内容
        html_content = self.downloader.download(root_url)
        new_urls=self.parser._parse_url(rootUrl,html_content)
        #把根页面的链接放入链接管理器
        self.urls.add_new_urls(new_urls)
    def craw(self):
        while self.urls.has_new_url():
            try:
                #从url管理器中获取一个链接
                new_url="%s%s"%("http://www.zhipin.com",self.urls.get_new_url())
                #下载页面内容
                html_content=self.downloader.download(new_url)
                #解析页面内容
                new_data=self.parser._parse_data(new_url,html_content)
                #内容存储到ES
                self.output._add_data_to_es(new_data)
            except Exception as e:
                print("error:",e)

if __name__ == '__main__':
    rootUrl="http://www.zhipin.com/c101010100/h_101010100/?page=1&ka=page-1"
    spider=SpiderMain()
    #解析根页面获取链接地址
    spider.craw_root(rootUrl)
    #解析子页面
    spider.craw()


