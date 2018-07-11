#!/usr/bin/env python3

'''
下载器
对指定的URL网页内容进行下载。
'''
from urllib import request
from star import HtmlParser,OutputManager
import time
import json
class HtmlDownLoader(object):
    def download(self,url,html_encode="utf-8"):
        print('begin down url is ',url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
                   'Referer':'http://v.qq.com/',
                   'Host':'v.qq.com'}
        try:
            req=request.Request(url,headers=headers)
            reponse=request.urlopen(req,timeout=2000)
            if reponse.getcode()!=200:
                return None
            # 获取页面内容
            html = reponse.read()
            # 获取页面编码
            # charset = chardet.detect(html);
            return html.decode(html_encode)
        except request.HTTPError as e:
            print(e.code)
        except request.URLError as e:
            print(e.reason)

if __name__ == '__main__':
    url="http://v.qq.com/doki/star?id=72781&tabid=2"
    html=HtmlDownLoader()
    data=html.download(url,'utf-8')
    print(data)
    parser=HtmlParser.HtmlParser()
    new_urls=parser._parse_url(url,data)
    print(new_urls)
    parser_data=parser._parse_data(url,data)
    # print(json.dumps(parser_data,ensure_ascii=False))
    out=OutputManager.OutputManager()
    out._add_data_to_es(parser_data)

