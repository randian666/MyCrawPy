#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re
import time
import datetime
from domain import Datum as da
from urllib.parse import urlparse

class HtmlParser(object):
    #获取指定页面的链接和内容
    def parse(self,url,content,html_encode="utf-8"):
        if url is None or content is None:
            return
        soup=BeautifulSoup(content,"html.parser",from_encoding=html_encode)
        new_urls=self._get_new_urls(soup)
        new_data=self._get_new_data(url,soup)
        return new_urls,new_data
    #获取指定页面符合要求的链接
    def _parse_url(self,url,content,html_encode="utf-8"):
        if url is None:
            return
        soup=BeautifulSoup(content,"html.parser",from_encoding=html_encode)
        new_urls=self._get_new_urls(soup)
        return new_urls
    #获取指定页面符合要求的内容
    def _parse_data(self,url,content,html_encode="utf-8"):
        if content is None:
            return
        soup=BeautifulSoup(content,"html.parser",from_encoding=html_encode)
        new_data=self._get_new_data(url,soup)
        return new_data
    #获取页面中符合要求的链接
    def _get_new_urls(self,soup):
        new_urls=set()
        links=soup.find_all("a",href=re.compile(r"/p_(\d+).html"))
        for link in links:
            url_path=link["href"]
            new_urls.add("https://www.qichacha.com"+url_path)
        return new_urls
    #获取数据
    def _get_new_data(self,url,soup):
        listDatum=[]
        try:
            datum=da.Datum()
            host = urlparse(url).netloc
            datum.host=host
            datum.url=url
            datum.created = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            title=soup.find("h1",class_="album-detail-title text-dark").get_text()
            if title is not None:
                datum.title=title
            contentStr=soup.find("div",class_="news-content text-dark m-b-lg")
            if contentStr is not None:
                datum.content=contentStr.prettify()
            sourceStr=soup.find("div",class_="panel-body").find("p").get_text()
            if sourceStr is not None:
                sourceOrTime=sourceStr.strip().split("|")
                if len(sourceOrTime)>0:
                    datum.source=sourceOrTime[0].strip().replace("来源：","")
                if len(sourceOrTime)>1:
                    publicTimeStr=sourceOrTime[1].strip().replace("发表于 ", "")
                    #把几天前转成时间
                    if "天前" in publicTimeStr:
                        timeCount = re.sub("\D", "", publicTimeStr)
                        realTime = datetime.date.today() - datetime.timedelta(days=int(timeCount))
                    datum.public_time=realTime
            listDatum.append(datum.__dict__)
        except  Exception as e:
            raise e
        return listDatum

if __name__ == '__main__':
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    print(yesterday)
    totalCount = '100abc'

    totalCount = re.sub("\D", "", totalCount)
    print(totalCount)
