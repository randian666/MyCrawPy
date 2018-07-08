#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re
import time

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
        links=soup.find_all("a",class_="people_avatar")
        for link in links:
            url_path=link["href"]
            new_urls.add("http:"+url_path+"&tabid=2")
        return new_urls
    #获取数据
    def _get_new_data(self,url,soup):
        data={"url":url,"source":"zhipin","created":time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())}
        try:
            job_primary=soup.find_all("div",class_="job-primary")
            detail_content=soup.find_all("div",class_="detail-content")
            info_company=soup.find_all("div",class_="info-company")
            location=soup.find("div",class_="location-address")
            if job_primary is None:
                return
            for p in job_primary:
                title=p.find("h1",class_="name")
                #标题
                data["title"]=title.contents[0]
                #工资
                data["wages"] = title.contents[1].get_text()
                tag=p.find("p")
                #地点
                data["place"] =tag.contents[0]
                #经验要求
                data["experience"] = tag.contents[2]
                #学历
                data["education"] = tag.contents[4]
                #职位标签
                job_tags=p.find("div",class_="job-tags").find_all("span")
                tags="";
                for tag in job_tags:
                    tags+=(tag.get_text()+"#")
                data["tags"] =tags
            for d in detail_content:
                content=d.find("div",class_="text")
                #职位描述
                data["content"]=content.get_text().strip()
            for c in info_company:
                company_name=c.find("h3",class_="name")
                tag = c.find_all("p")[0]
                url = c.find_all("p")[1]
                img=c.find("img").get("src")
                #公司名称
                data["company_name"]=company_name.get_text()
                #公司标签
                data["company_tag"]="%s#%s#%s"%(tag.contents[0],tag.contents[2],tag.contents[4].get_text())
                #公司网址
                data["company_url"]=url.get_text()
                #公司logo
                data["img"]=img
                #公司地址
            data["location"]=location.get_text()
        except  Exception as e:
            print(e)
        return data
