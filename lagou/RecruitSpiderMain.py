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
            url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false'
            datas = {
                'first': 'false',
                'pn': x,#页码
                'kd': '',#搜索关键字
            }
            info = self.lagou.get_json(url, datas)
            print(info)
            #职位信息结果写入es
            for data in info:
                self.output._add_data_to_es(json.dumps(data))
            print("第%s页正常采集，并写入ES。" % x)
if __name__ == '__main__':
    keyword = str(input('请输入你要抓取职位关键字：'))
    page = int(input('请输入你要抓取的页码总数：'))
    smain=SpiderMain()
    smain.craw(page)





