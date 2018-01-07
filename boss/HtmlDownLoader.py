#!/usr/bin/env python3

'''
下载器
对指定的URL网页内容进行下载。
'''
from urllib import request
from boss import HtmlParser

class HtmlDownLoader(object):
    def download(self,url,html_encode="utf-8"):
        print('begin down url is ',url)
        reponse=request.urlopen(url,timeout=2000)
        if reponse.getcode()!=200:
            return None
        #获取页面内容
        html=reponse.read()
        # 获取页面编码
        # charset = chardet.detect(html);
        return html.decode(html_encode)
if __name__ == '__main__':
    url="http://www.zhipin.com/job_detail/1416630940.html"
    html=HtmlDownLoader()
    data=html.download(url,'utf-8')
    parser=HtmlParser.HtmlParser()
    new_datas=parser._parse_data(url,data)
    print(new_datas)
