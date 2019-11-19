# -*- coding: utf-8 -*-
import scrapy
from xiaohuapro.items import XiaohuaproItem


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/meinvxiaohua/list121.html']

    # 创建一个模板URL
    module_url = 'http://www.521609.com/meinvxiaohua/list12%d.html'
    page_num = 1

    def parse(self, response):
        li_list = response.xpath('//div[@class="index_img list_center"]/ul/li')

        for li in li_list:
            title = li.xpath('./a[2]/b/text() | ./a[2]/text()').extract_first()
            detail_url = "http://www.521609.com" + li.xpath('./a[2]/@href').extract_first()

            # 我们可以直接将item理解成为一个字典,这个字典里面含有两个属性值,title和detail_url
            item = XiaohuaproItem()
            item["title"] = title
            item["detail_url"] = detail_url
            # print(item)  # {"title": title, "detail_url": detail_url}

            yield item

        # 在这里向其他页码发起请求，然后递归调用parse方法实现数据解析
        if self.page_num < 6:
            self.page_num += 1
            new_url = format(self.module_url % self.page_num)
            print("11111111111111", new_url)

            # 手动发送请求, 并递归调用parse解析方法
            # 在scrapy里面只会有两个地方用到yield，一个是向管道提交数据，另一个是手动发送请求时
            yield scrapy.Request(url=new_url, callback=self.parse)




