#!/usr/bin/env python3

'''
下载器
对指定的URL网页内容进行下载。
'''
from urllib import request
from lagou import HtmlParser
from common import OutputManager
import time
import ssl
import random

agent=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
       'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
       'Opera/8.0 (Windows NT 5.1; U; en)',
       'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
       'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2']
class HtmlDownLoader(object):
    def download(self,url,html_encode="utf-8"):
        time.sleep(1)
        context = ssl._create_unverified_context()
        print('begin down url is ',url)
        headers = {'User-Agent': random.choice(agent),
                   "Referer":url,
                   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
        try:
            req=request.Request(url,headers=headers)
            reponse=request.urlopen(req,timeout=2000,context=context)
            if reponse.getcode()!=200:
                return None
            # 获取页面内容
            html = reponse.read()
            # 获取页面编码
            return html.decode(html_encode)
        except request.HTTPError as e:
            print(e.code)
        except request.URLError as e:
            print(e.reason)

if __name__ == '__main__':
    url="https://www.lagou.com/zhaopin/HR/1/?filterOption=1"
    html=HtmlDownLoader()
    data=html.download(url,'utf-8')
    # print(data)
    parser=HtmlParser.HtmlParser()
    new_datas=parser._parse_data(url,data)
    print(new_datas)
    esManager=OutputManager.OutputManager()
    esManager._add_data_to_es(new_datas)
