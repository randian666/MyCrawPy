#!/usr/bin/env python3
'''
URL管理器
new_urls管理新的链接地址并且去重
used_urls管理已经爬取过的链接地址
'''
import redis
import time
import datetime

class UrlManager(object):
    def __init__(self):
        #新链接地址集合
        self.new_urls_key="new_urls_"+time.strftime('%Y-%m-%d',time.localtime())
        #已爬过的链接集合
        self.used_urls_key="used_urls_"+time.strftime('%Y-%m-%d',time.localtime())
        self.r = redis.Redis(host='203.76.214.3', port=6379,db=0,password='MX+A#3ADX$P',socket_timeout=1000)
    #添加链接地址
    def add_new_url(self,url):
        if url is None:
            return
        if self.r.sismember(self.new_urls_key,url) or self.r.sismember(self.used_urls_key,url):
            return
        try:
            self.r.sadd(self.new_urls_key,url);
        except Exception as e:
            print("error:" ,e)

    #批量添加链接地址
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    #判断是否还有链接
    def has_new_url(self):
        return self.r.scard(self.new_urls_key)>0
    #获取一个新的链接
    def get_new_url(self):
        #获取一个链接并且从redis中移除 返回的是一个bytes 需要转换成str
        temp_url=str(self.r.spop(self.new_urls_key),encoding = "utf-8")
        #存入已经爬过的链接key中
        self.r.sadd(self.used_urls_key,temp_url)
        return temp_url
if __name__ == '__main__':
    m=UrlManager();
    # m.add_new_url("www.jd.com")
    # print(m.has_new_url())
    # print(m.get_new_url())
    print(m.r.delete(m.used_urls_key))
    print(m.r.delete(m.new_urls_key))
    # print(m.r.scard(m.new_urls_key))
    # print(m.r.scard(m.used_urls_key))

