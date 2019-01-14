#!/usr/bin/env python3

'''
下载器
对指定的URL网页内容进行下载。
'''
from urllib import request
from qichacha import HtmlParser
from common import OutputManager
from urllib.parse import urlparse
import time
import ssl
import random
import requests

agent=['Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
       'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
       'Opera/8.0 (Windows NT 5.1; U; en)',
       'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
       'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2']
class HtmlDownLoader(object):
    def download(self,url,html_encode="utf-8"):
        #避免被反爬虫
        time.sleep(3)
        #支持https网站爬取
        context = ssl._create_unverified_context()
        print('begin down url is ',url)
        host = urlparse(url).netloc
        headers = {
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Host': host,
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
        }
        try:
            reqs = requests.get(url, headers=headers, timeout=30)
            if reqs.status_code!=200:
                return None
            return reqs.text
        except request.HTTPError as e:
            print(e.code)
        except request.URLError as e:
            print(e.reason)

if __name__ == '__main__':
    url="https://www.qichacha.com/news_index.shtml?p=1"
    html=HtmlDownLoader()
    data=html.download(url,'utf-8')
    # print(data)
    parser=HtmlParser.HtmlParser()
    new_urls =parser._parse_url(url, data)
    print(new_urls)
    # print(new_datas)
    # esManager=OutputManager.OutputManager()
    # esManager._add_data_to_es(new_datas)
