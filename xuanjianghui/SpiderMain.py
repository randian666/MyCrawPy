#!/usr/bin/env python3

from xuanjianghui import HtmlParser as p,OutputManager as o
from common import HtmlDownLoader as d

class SpiderMain(object):
    def __init__(self):
        #下载器
        self.downloader=d.HtmlDownLoader()
        #解析器
        self.parser=p.HtmlParser()
        #存储到ES
        self.output=o.OutputManager();
    def craw(self,page):
        for x in range(1, page + 1):
            try:
                url = 'http://my.yingjiesheng.com/index.php/personal/xjhinfo.htm/?page=%s&cid=&city=0&word=&province=0&schoolid=&sdate=&hyid=0'%(x)
                # 下载页面内容
                html_content = self.downloader.download(url,html_encode="gbk")
                # #解析页面内容
                new_data = self.parser._parse_data(url, html_content)
                # #内容存储到ES
                for json_data in new_data:
                    self.output._add_data_to_es(json_data)
            except Exception as e:
                print("error:",e)

if __name__ == '__main__':
    page = int(input('请输入你要抓取的页码总数：'))
    smain=SpiderMain()
    smain.craw(page)




