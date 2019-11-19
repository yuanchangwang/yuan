# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaohuaproItem(scrapy.Item):
    # define the fields for your item here like:
    # Field()方法其实就是一个万能参数，可以接收任何数据类型
    title = scrapy.Field()
    detail_url = scrapy.Field()

