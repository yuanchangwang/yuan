# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'  # 爬虫文件名称
    # allowed_domains = ['www.xxx.com']  # 允许发送请求的URL
    start_urls = ['http://www.budejie.com/text/']  # 起始URL

    def parse(self, response):
        li_list = response.xpath('//div[@class="j-r-list"]/ul/li')

        content_list = list()
        for li in li_list:
            # xpath表达式返回的一定是一个selector对象，如果要获取里面的数据的话，需要使用extract()方法
            # extract()方法返回的是一个复数(列表)
            # 如果你能够确定取到的列表里面的数据只有一条的话，就可以直接使用extract_first()方法来获取
            content = li.xpath('./div[2]/div/a/text()').extract_first()
            dic = {
                "content": content
            }
            content_list.append(dic)

        return content_list
