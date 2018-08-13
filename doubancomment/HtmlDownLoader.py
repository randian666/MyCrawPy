#!/usr/bin/env python3

'''
下载器
对指定的URL网页内容进行下载。
'''
from urllib import request
from doubancomment import HtmlParser,DoubanLogin as lg
import ssl
import requests

class HtmlDownLoader(object):
    def download(self,url,session,html_encode="utf-8"):
        print('begin down url is ', url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Referer': 'https://movie.douban.com/',
            'Host': 'movie.douban.com'}
        try:
            content=session.get(url)
            return content.text;
        except request.HTTPError as e:
            print(e.code)
        except request.URLError as e:
            print(e.reason)
if __name__ == '__main__':
    url="https://movie.douban.com/subject/26366496/comments?start=60&limit=20&sort=new_score&status=P"
    html=HtmlDownLoader()
    session=lg.DoubanLogin().login();
    data=html.download(url,session,'utf-8')
    parser=HtmlParser.HtmlParser()
    new_datas=parser.parse(url,data)
    # print(new_urls)
    print(new_datas)
