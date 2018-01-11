#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib import request
import random

'''
获取代理ip
'''
class CrawProxy(object):
    def _get_ip_list(self):
        url = 'http://www.xicidaili.com/nn/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        try:
            req=request.Request(url,headers=headers)

            reponse=request.urlopen(req,timeout=2000)
            if reponse.getcode()!=200:
                return None
            # 获取页面内容
            html = reponse.read()
            soup = BeautifulSoup(html, "html.parser", from_encoding="UTF-8")
            table_ip=soup.find("table",attrs={"id":"ip_list"})
            ips = table_ip.find_all('tr')
            ip_list = []
            for i in ips:
                tds=i.find_all('td')
                if len(tds)>3:
                    ip_list.append(tds[1].text+':'+tds[2].text)
            return ip_list
        except request.HTTPError as e:
            print(e.code)
        except request.URLError as e:
            print(e.reason)
    def _get_random_ip(self,ip_list):
        proxy_ip=random.choice(ip_list)
        proxies={"http":proxy_ip}
        return proxies
if __name__ == '__main__':
    proxy=CrawProxy()
    iplist=proxy._get_ip_list()
    print(iplist)
    print(proxy._get_random_ip(iplist))
