#!/usr/bin/env python3.4

# encoding: utf-8

"""

Created on 19-9-18

@title: ''

@author: Liu.Xun

"""

import time
import uuid

import requests

from lagou import HtmlParser as p
from common import UrlManager as u,HtmlDownLoader as d

class lagouMain(object):
    def __init__(self):
        # url链接管理器
        self.old_urls = set()  # 已爬取的Url集合

    # 获取存储职位信息的json对象，遍历获得公司名、福利待遇、工作地点、学历要求、工作类型、发布时间、职位名称、薪资、工作年限
    def get_json(self, url, datas):
        my_headers = {

            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",

            "Referer": "https://www.lagou.com/jobs/list_Python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",

            "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8"

        }

        time.sleep(5)

        ses = requests.session()  # 获取session

        ses.headers.update(my_headers)  # 更新

        ses.get("https://www.lagou.com/jobs/list_python?px=new&city=%E5%85%A8%E5%9B%BD#order")

        content = ses.post(url=url, data=datas)

        result = content.json()
        info = result['content']['positionResult']['result']
        print(info)
        listinfo = []
        # listCompany=[]
        for job in info:
            information = {}
            information['uuid'] = str(uuid.uuid1())
            information['userId'] = "148"
            information['firmId'] = ""  # 所属公司编号
            information['online'] = ""  # 在线状态
            information['jobId'] = "-1"  # 职位类型编号
            information['cityId'] = ""  # 企业办公地方编号
            information['hcTotal'] = "-1"  # 招聘人数
            information['workType'] = ""  # 工作性质标签
            information['workEdu'] = ""  # 学历要求类型ID
            information['workWage'] = ""  # 工资区间编号
            information['workYear'] = ""  # 年限编号编号
            information['audit'] = ""  # 审核状态
            information['viewTotal'] = ""  # 访问人数
            information['sort'] = "1"  # 排序权重
            information['sourceId'] = '11'  # 数据来源
            information['sourceName'] = '拉勾'  # 数据来源
            information['createTime'] = (job['createTime'])  # 创建时间
            information['updateTime'] = (job['createTime'])  # 更新时间
            information['workTypeLabel'] = (job['jobNature'])  # 工作性质
            information['longitude'] = (job['longitude'])  # 经度
            information['latitude'] = (job['latitude'])  # 纬度
            information['cityName'] = (job['city'])  # 岗位对应城市
            information['firmName'] = (job['companyFullName'])  # 公司全名
            information['firmLogo'] = (job['companyLogo'])  # 公司logo
            information['affordTags'] = ",".join(job['companyLabelList'])  # 福利待遇
            information['skillTags'] = ",".join(job['skillLables'])  # 技能要求
            information['cityAddress'] = (job['district'])  # 工作地点
            information['workEduLabel'] = (job['education'])  # 学历要求
            # information['']=(job['firstType'])  # 工作类型
            # information['']=(job['formatCreateTime'])  # 发布时间
            information['jobName'] = (job['positionName'])  # 职位名称
            information['workWageLabel'] = (job['salary'])  # 薪资
            information['workYearLabel'] = (job['workYear'])  # 工作年限
            fin_url = r'http://www.lagou.com/jobs/%s.html' % job['positionId']
            information['detail_url'] = (fin_url)  # 职位详情页
            job_detail_txt, job_detail_html = self.get_content(fin_url)
            if job_detail_txt is None or len(job_detail_txt) == 0:
                time.sleep(5)
                job_detail_txt, job_detail_html = self.get_content(job['positionId'])
            information['jobDescription'] = (job_detail_txt)  # 工作描述
            information['jobDuty'] = job_detail_html  # 工作职责
            information['companyId']=job['companyId']     # 公司ID
            listinfo.append(information)
        return listinfo

    '''
    获取职位描述
    获取职位页面，由PositionId和BaseUrl组合成目标地址
    '''

    def get_content(self, fin_url):
        print(fin_url)
        reqs = self.get_response_url(fin_url)
        job_detail_txt, job_detail_html = p._parse_jobdetail(reqs.text)
        return job_detail_txt, job_detail_html

    '''
    获取企业信息
    '''
    def get_firm(self, companyId):
        firm_url = r'http://www.lagou.com/gongsi/%s.html' % companyId
        # url防重
        if firm_url in self.old_urls:
            return None
        reqs = self.get_response_url(firm_url)
        companyInfo = p._parse_companydetail(firm_url, reqs.text)
        companyInfo['companyId'] = companyId  # 公司ID
        self.old_urls.add(firm_url)
        return companyInfo

    def get_response_url(self, url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=ABAAABAAAGGABCB377740F4A9A65EF019AD783BC58F334E; user_trace_token=20190916172217-efbd0ff4-8180-4f90-bab0-21f77665d3e0; WEBTJ-ID=20190916172218-16d396142b531c-02cceedde30fdf-67e153a-2073600-16d396142b655e; _ga=GA1.2.1590732834.1568625739; _gid=GA1.2.1283055215.1568625739; LGUID=20190916172218-7b0f270d-d863-11e9-9245-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; X_MIDDLE_TOKEN=39934203dafd406c3448ad0498cb4b93; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d39628ec53b5-0761ff6c727cbe-67e153a-2073600-16d39628ec62d3%22%2C%22%24device_id%22%3A%2216d39628ec53b5-0761ff6c727cbe-67e153a-2073600-16d39628ec62d3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2277.0.3865.75%22%7D%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1568625739,1568794783; LGSID=20190919113615-a292a19b-da8e-11e9-937f-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2Fyouxidonghua%2F2%2F%3FfilterOption%3D2; gate_login_token=b2e199eaa1e26c970cfe9ce63e1c75b08ef1e77c5f965526; _putrc=47887982C327011A; login=true; unick=%E5%88%98%E5%8B%8B; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; _gat=1; TG-TRACK-CODE=index_search; SEARCH_ID=0524b17be7064fddb20bbbb2afe7a8ba; X_HTTP_TOKEN=5e077b26a9293a145264688651a61f0edfacedb2f5; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1568864626; LGRID=20190919114345-ae98c7fe-da8f-11e9-9383-525400f775ce',
            'Host': 'www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_python?px=new&city=%E5%85%A8%E5%9B%BD',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
        }
        print(url)
        ses = requests.session()  # 获取session
        ses.headers.update(headers)  # 更新
        ses.get("https://www.lagou.com/jobs/list_python?px=new&city=%E5%85%A8%E5%9B%BD#order")
        reqs = ses.get(url, headers=headers, timeout=30)
        return reqs

    def get_showid(self,url):
        downloader = d.HtmlDownLoader()
        content=downloader.download(url)
        return p._parse_showid(url,content)

if __name__ == '__main__':
    lg = lagouMain()
    lg.get_firm('84440587')
