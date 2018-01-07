#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re

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
        links=soup.find_all("a",href=re.compile(r"/subject/\d+/$"))
        for link in links:
            url_path=link["href"]
            new_urls.add(url_path)
        return new_urls
    #获取数据
    def _get_new_data(self,url,soup):
        data={"url":url}
        title_data=soup.find("span",attrs={"property":"v:itemreviewed"})
        if title_data is None:
            return
        data["title"]=title_data.get_text()
        content_data=soup.find("div",class_="intro")
        if content_data is None:
            return
        data["content"]=content_data.get_text()
        return data
