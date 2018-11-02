# -*- coding: utf-8 -*-
import scrapy


class SoufangSpider(scrapy.Spider):
    name = 'soufang'
    allowed_domains = ['fang.com']
    start_urls = ['http://fang.com/']

    def parse(self, response):
        pass
