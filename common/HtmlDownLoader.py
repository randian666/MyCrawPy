#!/usr/bin/env python3

'''
下载器
对指定的URL网页内容进行下载。
'''
from urllib import request
from qichacha import HtmlParser
from urllib.parse import urlparse
import time
import requests

class HtmlDownLoader(object):
    def download(self,url,html_encode="utf-8"):
        #避免被反爬虫
        time.sleep(3)
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
