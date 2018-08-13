#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re

class HtmlParser(object):
    #获取指定页面的链接和内容
    def parse(self,url,content,html_encode="utf-8"):
        if url is None or content is None:
            return
        soup=BeautifulSoup(content,"html.parser")
        new_data=self._get_new_data(url,soup)

        return new_data
    #获取数据
    def _get_new_data(self,url,soup):
        datas=[]
        comments = soup.find("div",id="comments").find_all("div", class_="comment-item")
        for comment in comments:
            data = {"name":"","see":"","time":"","rating":"","content":""}
            name=comment.find("span",class_="comment-info").find("a")
            if name is not None:
                data["name"]=name.get_text().strip()
            see = comment.find("span", class_="comment-info").find("span")
            if see is not None:
                data["see"]=see.get_text().strip()
            rating = comment.find("span", class_="comment-info").find("span",class_="rating")
            if rating is not None:
                data["rating"]=rating.get("title").strip()
            time = comment.find("span", class_="comment-info").find("span", class_="comment-time ").get_text()
            if time is not None:
                data["time"]=time.strip()
            content=comment.find("span",class_="short")
            if content is not None:
                data["content"]=content.get_text().strip()
            datas.append(data)
        return datas