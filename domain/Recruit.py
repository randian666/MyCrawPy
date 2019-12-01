#!/usr/bin/env python3
import json

class Recruit(object):

    def __init__(self):
        #url
        self.url=None
        #host
        self.host=None
        #所属城市
        self.suggestCity=None
        #数据来源
        self.source=None
        #爬取时间
        self.created=None
        #职位名称
        self.title=None
        #职位描述
        self.job_detail=None
        #薪水
        self.salary=None
        #职位URL
        self.job_url=None
        #职位类型
        self.job_type=None
        #职位地点
        self.place=None
        #经验
        self.experience=None
        #教育
        self.education=None
        #所属公司
        self.company=None
        #公司URL
        self.company_url=None
        #公司类型
        self.company_type=None
        #公司融资情况
        self.company_financing=None
        #公司规模
        self.company_size=None
        #更新时间
        self.publis_time=None
        #关键字
        self.keyword=None
        #备注
        self.remark=None

if __name__ == '__main__':
    r=Recruit()
    r.url="100"
    print(r.url)
    print(r.__dict__)
