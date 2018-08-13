#!/usr/bin/env python3

from doubancomment import HtmlDownLoader as d,HtmlParser as p,OutputManager as o,DoubanLogin as lg
import time
class SpiderMain(object):
    def __init__(self):
        #登陆
        self.dblogin=lg.DoubanLogin();
        #下载器
        self.downloader=d.HtmlDownLoader()
        #解析器
        self.parser=p.HtmlParser()
        #存储
        self.output=o.OutputManager();
    def craw_root(self,root_url,session):
        # 下载根页面内容
        try:
            # 下载页面内容
            html_content = self.downloader.download(root_url,session)
            # 解析页面内容
            new_data = self.parser.parse(root_url, html_content)
            # 内容存储到csv
            self.output._add_data_to_csv(new_data)
        except Exception as e:
            print("error:", e)

if __name__ == '__main__':
    spider = SpiderMain()
    session=spider.dblogin.login();
    print("登陆成功，开始爬爬爬。。。。")
    i=1
    while(i<26):
        offset=(i-1)*20
        rootUrl="https://movie.douban.com/subject/26366496/comments?start={}&limit=20&sort=new_score&status=P".format(offset)
        #解析根页面获取链接地址
        spider.craw_root(rootUrl,session)
        i=i+1
        #5秒钟爬一次
        time.sleep(5)



