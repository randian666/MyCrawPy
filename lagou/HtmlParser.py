#!/usr/bin/env python3
from bs4 import BeautifulSoup
import uuid
import hashlib

#获取指定页面的链接和内容
def _parse_jobdetail(html_content,html_encode="utf-8"):
    soup = BeautifulSoup(html_content, "html.parser", from_encoding=html_encode)
    job_detail = soup.select_one(".job_detail>.job_bt")
    content=""
    content_html=""
    if job_detail is not None:
        content=job_detail.get_text()
        content_html=job_detail.prettify()
    return content,content_html

#获取公司信息
def _parse_companydetail(url,html_content,html_encode="utf-8"):
    soup = BeautifulSoup(html_content, "html.parser", from_encoding=html_encode)
    companyDetail = {}
    companyDetail['id']=hashlib.md5(url.encode(encoding='UTF-8')).hexdigest()
    companyDetail['uuid'] = str(uuid.uuid1())
    companyDetail['userId'] = "148"
    companyDetail['url'] = url
    ele_company_info=soup.find("div",class_="company_info")
    ele_name=ele_company_info.select_one(".company_main>h2>a")
    if ele_name is not None:
        #企业主页
        if ele_name.has_key('href'):
            companyDetail["index"]=ele_name['href']
        #企业名称
        companyDetail["name"]=ele_name['title']
        #公司别名
        companyDetail["alias"]=ele_name.get_text().strip()
    # 公司签名
    ele_company_word=ele_company_info.select_one(".company_main>.company_word")
    if ele_company_word is not None:
        companyDetail["signature"] = ele_company_word.get_text().strip()
    #企业logo
    ele_logo=soup.select_one(".top_info_wrap>img")
    if ele_logo is not None:
        companyDetail["logo"]="http:"+ele_logo["src"]

    ele_tags_container=soup.find("div",id="tags_container")
    if ele_tags_container is not None:
        ele_tags=ele_tags_container.find_all("li")
        #企业标签
        tags_list=[]
        for tag in ele_tags:
            tags_list.append(tag.get_text().strip())
        companyDetail["tags"]=",".join(tags_list)
    #公司介绍
    ele_company_content=soup.find("span",class_="company_content")
    if ele_company_content is not None:
        companyDetail["introduce"]=ele_company_content.get_text()

    ele_item_content=soup.find("div",id="basic_container").find("div",class_="item_content")
    li_item_content=ele_item_content.find_all('li')
    if li_item_content is not None:
        #行业
        if len(li_item_content)>=1:
            companyDetail["industryTag"] =li_item_content[0].get_text().strip()
        #融资规模
        if len(li_item_content)>=2:
            companyDetail["investLabel"] = li_item_content[1].get_text().strip()
        #公司规模
        if len(li_item_content)>=3:
            companyDetail["scaleLabel"] = li_item_content[2].get_text().strip()
        #公司地点
        if len(li_item_content)>=4:
            companyDetail["cityName"] = li_item_content[3].get_text().strip()
    ele_cityAddr=soup.select_one(".mlist_li_desc")
    if ele_cityAddr is not None:
        companyDetail["cityAddress"]=ele_cityAddr.get_text().strip()
    print(companyDetail)
    return companyDetail

def _parse_showid(url,html_content,html_encode="utf-8"):
    soup = BeautifulSoup(html_content, "html.parser", from_encoding=html_encode)
    ele_company_list=soup.find("div",id="company_list")
    ele_a=ele_company_list.find_all("a")
    return ele_a[0].get('data-lg-webtj-_show_id')