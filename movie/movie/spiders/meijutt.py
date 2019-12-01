# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieItem


"""
    scrapy初始Url的两种写法，
    一种是常量start_urls，并且需要定义一个方法parse（）
    另一种是直接定义一个方法：star_requests()
"""
class MeijuttSpider(scrapy.Spider):
    name = 'meijutt'
    allowed_domains = ['meijutt.com']

    '''
    由此方法通过下面链接爬取页面
    '''
    def start_requests(self):
        # 定义爬取的链接
        urls = [
            'https://www.meijutt.com/new100.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)  # 爬取到的页面如何处理？提交给parse方法处理

    def parse(self, response):
        '''
       scrapy运行的流程：
       1、定义链接；
       2、通过链接爬取（下载）页面；
       3、定义规则，然后提取数据；
       就是这么个流程，似不似很简单呀？
       '''
        movies=response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movies:
            item = MovieItem()
            item['name']=movie.xpath('./h5/a/text()').extract_first()
            yield item
            print(item['name'])