#!/usr/bin/env python3
from bs4 import BeautifulSoup
import json
import uuid

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
            content=soup.select_one(".campus-detail")
            ele_trs=content.find_all("tr")
            listinfo = []
            for tr in ele_trs:
                information = {}
                information['uuid'] = str(uuid.uuid1())
                information['userId'] = "148"
                information['city_name']=tr.contents[1]
                information['city_name'] = tr.contents[1]
                information['stime']=tr.contents[2]
                print(tr.contents[1])
            return content
        except  Exception as e:
            print(e)


<resultMap id="BaseResultMap" type="com.beyond.platform.module.hunter.entity.Preach">
  <id column="id" property="id" />
  <result column="uuid" property="uuid" />
  <result column="user_id" property="userId" />
  <result column="type" property="type" />
  <result column="image" property="image" />
  <result column="title" property="title" />
  <result column="video" property="video" />
  <result column="introduce" property="introduce" />
  <result column="content" property="content" />
  <result column="address" property="address" />
  <result column="year" property="year" />
  <result column="month" property="month" />
  <result column="day" property="day" />
  <result column="stime" property="stime" />
  <result column="etime" property="etime" />
  <result column="tags" property="tags" />
  <result column="city_id" property="cityId" />
  <result column="city_name" property="cityName" />
  <result column="firm_id" property="firmId" />
  <result column="firm_name" property="firmName" />
  <result column="school_id" property="schoolId" />
  <result column="school_name" property="schoolName" />
  <result column="link" property="link" />
  <result column="enabled" property="enabled" />
  <result column="create_time" property="createTime" />
  <result column="update_time" property="updateTime" />
 </resultMap>