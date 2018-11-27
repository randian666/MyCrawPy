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
        links=soup.find_all("a",href=re.compile(r'https://www.lagou.com/zhaopin/(\w+)/'))
        for link in links:
            url_path=link["href"]
            new_urls.add(url_path)
        return new_urls

        # 获取数据
    def _get_new_data(self, url, soup):
        listJob = []
        try:
            keywords=soup.find(attrs={"name": "keywords"})
            if keywords is not None:
                keywords = keywords['content']
            inputKey=soup.find('input',id='keyword')
            if inputKey is not None:
                inputKey=inputKey['value']
            joblist = soup.find('div', class_='s_position_list ')
            if joblist is None:
                return listJob
            ul = joblist.find('ul',class_='item_con_list')
            if ul is None:
                return listJob
            li = ul.find_all('li')
            for l in li:
                d = recruit.Recruit()
                d.job_type=inputKey
                d.keyword=keywords
                d.url = url
                d.suggestCity = "北京站"
                d.source = "拉勾"
                d.created = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                primary = l.find('div', class_='p_top')
                if primary is not None:
                    d.title = primary.find('h3').get_text()
                    place=primary.find('span', class_='add')
                    if len(place.contents)>0:
                        d.place = place.contents[1].get_text()
                    d.publis_time =primary.find('span',class_='format-time').get_text()
                    d.job_url=primary.find('a',class_='position_link')['href']

                bot=l.find('div',class_='p_bot')
                if bot is not None:
                    libl=bot.find('div', class_='li_b_l')
                    if len(libl.contents)>0:
                        d.salary =libl.contents[1].get_text()
                        d.experience=libl.contents[4].split("/")[0].strip()
                        d.education=libl.contents[4].split("/")[1].strip()

                company=l.find('div',class_='company')
                if company is not None:
                    company_name=company.find('div', class_='company_name')
                    d.company =company_name.get_text().strip()
                    d.company_url =company_name.find('a')['href']
                    industry=company.find('div',class_='industry')

                    listIndustry=industry.get_text().split('/')
                    if len(listIndustry)>0:
                        d.company_type=industry.get_text().split('/')[0].strip()
                    if len(listIndustry)>1:
                        d.company_financing = industry.get_text().split('/')[1].strip()
                    if len(listIndustry)>2:
                        d.company_size = industry.get_text().split('/')[2].strip()
                listJob.append(d.__dict__)
        except  Exception as e:
            print(e)
        return listJob
