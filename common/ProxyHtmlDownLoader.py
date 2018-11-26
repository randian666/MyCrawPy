#!/usr/bin/env python3

'''
下载器
对指定的URL网页内容进行下载。
'''
from urllib import request
from boss import HtmlParser
import time
import ssl

class ProxyHtmlDownLoader(object):
    def download(self,url,proxy,html_encode="utf-8"):
        try:
            context = ssl._create_unverified_context()
            # 创建ProxyHandler
            proxy_support = request.ProxyHandler(proxy)
            # 创建Opener
            opener = request.build_opener(proxy_support)
            # 添加User Angent
            opener.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36')]
            # 安装OPener
            request.install_opener(opener)
            # 使用自己安装好的Opener
            response = request.urlopen(url,context=context)
            # 读取相应信息并解码
            html = response.read().decode(html_encode)
            # 打印信息
            print(html)
            return html
        except request.HTTPError as e:
            print(e.code)
        except request.URLError as e:
            print(e.reason)
            self.download()
if __name__ == '__main__':
    url="http://www.zhipin.com/job_detail/1416704802.html"
    html=ProxyHtmlDownLoader()
    proxy = {'http': '183.230.145.112:8888'}
    data=html.download(url,proxy)
    parser=HtmlParser.HtmlParser()
    new_datas=parser._parse_data(url,data)
    print(new_datas)
