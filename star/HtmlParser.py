#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re
import time
import json

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
        data={"url":url,"source":"v.qq.com","created":time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())}
        star_info = {}
        star_image=[]
        star_related=[]
        try:
            #头像
            star_pic=soup.find("div",class_="star_pic").find("img")["src"]
            data["star_pic"]=star_pic
            #姓名
            name=soup.find("div",class_="star_name")
            data["name"]=name.get_text()
            #百科
            wiki_content=soup.find("div",class_="wiki_content")
            data["wiki_content"]=wiki_content.get_text()
            #艺人信息
            line=soup.find("div",class_="wiki_info_1").find_all("div",class_="line")
            for s in line:
               lable=s.find("span",class_="lable").get_text()
               content = s.find("span", class_="content").get_text()
               star_info[lable]=content
            line2 = soup.find("div", class_="wiki_info_2").find_all("div", class_="line")
            for s in line2:
               lable=s.find("span",class_="lable").get_text()
               content = s.find("span", class_="content").get_text()
               star_info[lable]=content
            if star_info:
                data["star_info"]=json.dumps(star_info,ensure_ascii=False)
            #艺人高清大图
            imges=soup.find("div",class_="mod_pics_waterfall").find_all("span",class_="pic_item")
            for i in imges:
                star_image.append(i["data-pic"])
            data["star_image"]=star_image
            #相关明星
            peoples=soup.find("div",class_="mod_people_inner").find_all("div",class_="people_item")
            for p in peoples:
                partner_info={}
                partner=p.find("span",class_="people_partner").get_text()
                name=p.find("a",class_="people_name").get_text()
                image=p.find("img",class_="avatar_pic")["src"]
                partner_info[partner]=name
                partner_info["image"]=image
                star_related.append(partner_info)
            data["star_related"]=json.dumps(star_related,ensure_ascii=False)
        except  Exception as e:
            print(e)
        return data
