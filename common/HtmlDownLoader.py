#!/usr/bin/env python3

'''
下载器
对指定的URL网页内容进行下载。
'''
from urllib import request
from morningstar import HtmlParser
from urllib.parse import urlparse
import time
import requests

class HtmlDownLoader(object):
    def download(self,url,html_encode="utf-8",headersArgs=None):
        #避免被反爬虫
        time.sleep(1)
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
        if headersArgs is not None:
            headers={**headers,**headersArgs}
        try:
            reqs = requests.get(url, headers=headers, timeout=30)
            reqs.encoding=html_encode
            if reqs.status_code!=200:
                return None
            return reqs.text
        except request.HTTPError as e:
            print(e.code)
        except request.URLError as e:
            print(e.reason)

if __name__ == '__main__':
    url="http://www.lagou.com/jobs/5617112.html?show=13cb3d09998246c0895dd6e4433077b5"
    html=HtmlDownLoader()
    data=html.download(url,'utf-8')
    print(data)

