# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieItem
class MeijuttSpider(scrapy.Spider):
    name = 'meijutt'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        movies=response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movies:
            item = MovieItem()
            item['name']=movie.xpath('./h5/a/text()').extract_first()
            yield item
            print(item['name'])