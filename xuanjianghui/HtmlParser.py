#!/usr/bin/env python3
from bs4 import BeautifulSoup
import json
import uuid

import requests
import pytesseract
from PIL import Image
from io import BytesIO

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
                ele_td=tr.find_all("td")
                # response = requests.get(img_url)
                # image = Image.open(BytesIO(response.content))
                # # image.show()
                # code = pytesseract.image_to_string(image,lang='eng')
                # print(code)
                information = {}
                information['uuid'] = str(uuid.uuid1())
                information['userId'] = "148"
                if ele_td[0] is not None:
                    information['city_name']=ele_td[0].get_text()
                if ele_td[1] is not None:
                    information['stime']=ele_td[1].get_text()[0:10]
                if ele_td[2] is not None:
                    img_url="http://my.yingjiesheng.com"+ele_td[2].find('img').get('src')
                    information['stime_hours']=img_url
                if ele_td[3] is not None:
                    information['firm_name']=ele_td[3].get_text()
                if ele_td[4] is not None:
                    information['school_name'] = ele_td[4].get_text()
                if ele_td[5] is not None:
                    information['address'] = ele_td[5].get_text()
                if ele_td[6] is not None:
                    information['link'] = ele_td[6].find('a').get('href')
                listinfo.append(information)
            return listinfo
        except  Exception as e:
            print(e)