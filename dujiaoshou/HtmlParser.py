#!/usr/bin/env python3
from bs4 import BeautifulSoup
import json

class HtmlParser(object):
    #获取指定页面符合要求的内容
    def _parse_data(self,url,content,html_encode="utf-8"):
        if content is None:
            return
        soup=BeautifulSoup(content,"html.parser",from_encoding=html_encode)
        new_data=self._get_new_data(url,soup)
        return new_data
        # 获取数据
    def _get_new_data(self, url, soup):
        try:
            content=soup.find('script',id='__NEXT_DATA__').get_text().strip()
            jsonContent=json.loads(content)
            companies=jsonContent['props']['pageProps']['companies']
            return companies
        except  Exception as e:
            print(e)
