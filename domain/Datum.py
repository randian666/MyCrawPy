#!/usr/bin/env python3

class Datum(object):

    def __init__(self):
        #URL
        self.url=""
        #HOST
        self.host=""
        #来源
        self.source=""
        #创建时间
        self.created=""
        #标题
        self.title=""
        #内容
        self.content=""
        #关键字
        self.keyword=""
        #发表时间
        self.public_time=""
        #备注
        self.remark=""

if __name__ == '__main__':
    r=Datum()
    r.url="100"
    print(r.url)
    print(r.__dict__)