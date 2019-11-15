#!/usr/bin/env python3

from lagou import lagouMain as lg, OutputManager as out
import json

class SpiderMain(object):
    def __init__(self):
        #存储到ES
        self.output=out.OutputManager()
        #lg爬取器
        self.lagou=lg.lagouMain()
    def craw(self,page):
        for x in range(1, page + 1):
            url = 'https://www.lagou.com/gongsi/0-0-0-0.json'
            datas ={
                'first':'false',
                'pn':str(page),
                'sortField':'0',
                'havemark':'0'
                }
            companyList = self.lagou.get_company_json(url, datas)
            #公司信息结果写入es
            # for company in companyList:
            #     self.output._add_company_to_es(json.dumps(company))
            print("第%s页正常采集，并写入ES。" % x)
if __name__ == '__main__':
    # page = int(input('请输入你要抓取的页码总数：'))
    smain=SpiderMain()
    smain.craw(1)





