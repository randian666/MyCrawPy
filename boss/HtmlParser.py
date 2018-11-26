#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re
import time
from common import Recruit as recruit

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
        links=soup.find_all("a",href=re.compile(r"/c101010100-p(\d+)/"))
        for link in links:
            url_path=link["href"]
            new_urls.add(url_path)
        return new_urls
    #获取数据
    def _get_new_data(self,url,soup):
        listJob=[]
        try:
            joblist=soup.find('div',class_='job-list')
            if joblist is None:
                return
            ul=joblist.find('ul')
            li=ul.find_all('li')
            for l in li:
                d =recruit.Recruit()
                d.url=url
                d.suggestCity="北京站"
                d.source="BOSS直聘"
                d.created=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                # data = {"url": url,"suggestCity":"北京站","source": "BOSS直聘", "created": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}
                primary =l.find('div',class_='info-primary')
                if primary is not None:
                    d.title=primary.find('div',class_='job-title').get_text()
                    d.salary=primary.find('span',class_='red').get_text()
                    a=primary.find_all('a')[0]
                    d.job_url="https://www.zhipin.com"+a["href"]
                    infoPrimary=primary.find('p')
                    if len(infoPrimary.contents)>0:
                        d.place = infoPrimary.contents[0]
                    if len(infoPrimary.contents) > 2:
                        d.experience = infoPrimary.contents[2]
                    if len(infoPrimary.contents) > 4:
                        d.education = infoPrimary.contents[4]
                company =l.find('div',class_='info-company')
                if company is not None:
                    d.company = company.find_all('a')[0].get_text()
                    d.company_url = "https://www.zhipin.com" + company.find_all('a')[0]["href"]
                    infoCompany = company.find('p')
                    if len(infoCompany.contents)>0:
                        d.company_type=infoCompany.contents[0]
                    if len(infoCompany.contents)>2:
                        d.company_financing=infoCompany.contents[2]
                    if len(infoCompany.contents)>4:
                        d.company_size=infoCompany.contents[4]
                publis=l.find('div',class_='info-publis')
                if publis is not None:
                    d.publis_time=publis.find('p').get_text()
                listJob.append(d.__dict__)
        except  Exception as e:
            raise e
        return listJob
