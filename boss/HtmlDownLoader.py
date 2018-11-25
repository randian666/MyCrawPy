#!/usr/bin/env python3

'''
下载器
对指定的URL网页内容进行下载。
'''
from urllib import request
from boss import HtmlParser
from boss import OutputManager
import time
import ssl

class HtmlDownLoader(object):
    def download(self,url,html_encode="utf-8"):
        time.sleep(2)
        context = ssl._create_unverified_context()
        print('begin down url is ',url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                   "Accept-Encoding":"gzip",
                   "Accept-Language":"zh-CN,zh;q=0.8",
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
    url="https://www.zhipin.com/c101010100-p100101/?page=1&ka=page-1"
    html=HtmlDownLoader()
    data=html.download(url,'utf-8')
    # print(data)
    parser=HtmlParser.HtmlParser()
    new_datas=parser._parse_data(url,data)
    print(new_datas)
    esManager=OutputManager.OutputManager()
    esManager._add_data_to_es(new_datas)
