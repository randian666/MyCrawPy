#!/usr/bin/env python3

'''
post请求下载器
对指定的URL网页内容进行下载。
'''
from urllib import request
from urllib.parse import urlparse
import time
import requests
import json

class HtmlDownLoader(object):
    def download(self,url,data,html_encode="utf-8",headersArgs=None):
        #避免被反爬虫
        time.sleep(3)
        headers = {}
        if headersArgs is not None:
            headers={**headers,**headersArgs}
        try:
            data_body=json.dumps(data)
            print('begin down url is ', url,'body is ',data_body)
            reqs = requests.post(url,data=data_body,headers=headers, timeout=30)
            if reqs.status_code!=200:
                return None
            return reqs.text
        except request.HTTPError as e:
            print(e.code)
        except request.URLError as e:
            print(e.reason)

if __name__ == '__main__':
     d=HtmlDownLoader();
     data={}
     data['pn'] = 1
     data['first'] = 'false'
     data['sid'] = '10b91c2e79994b078757e5d214ba98f62'
     result=d.download('https://www.lagou.com/jobs/positionAjax.json?px=new&city=北京&needAddtionalResult=false',data)
     print(result)

