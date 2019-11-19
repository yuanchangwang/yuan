# -*- coding: utf-8 -*-
import scrapy


class PostdemoSpider(scrapy.Spider):
    name = 'postdemo'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://fanyi.baidu.com/sug']

    def start_requests(self):
        data = {
            'kw': 'dog'
        }
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url, callback=self.parse, formdata=data)

    def parse(self, response):
        print(response.text)
