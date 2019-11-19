# -*- coding: utf-8 -*-
import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.baidu.com/s?wd=ip']

    def parse(self, response):
        # ip = response.xpath('//*[@id="1"]/div[1]/div[1]/div[2]/table/tbody/tr/td/span/text()').extract_first()
        # print(response.url + "对应的IP为: " + ip)
        page_text = response.text
        with open('./ip.html', 'w', encoding='utf-8') as fp:
            fp.write(page_text)
