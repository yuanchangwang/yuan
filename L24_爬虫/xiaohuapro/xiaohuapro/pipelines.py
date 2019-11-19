# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import redis
import pymysql


class XiaohuaproPipeline(object):
    """
    将解析到的数据存储到txt文件中
    """
    f = None

    def open_spider(self, spider):
        print("开始爬虫")
        self.f = open('./xiaohua.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(item["title"] + "--" + item["detail_url"] + "\n")
        return item  # 这个return非常重要，可以将item传递给下一个管道类

    def close_spider(self, spdier):
        self.f.close()
        print("结束爬虫")


class MysqlPipeline(object):
    """
    将解析到的数据存储到mysql数据中
    """
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='192.168.1.197', port=3306, user='root', password='redhat', db='xiaohua', charset="utf8")
        print(self.conn)

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            sql = 'insert into xiaohua values ("%s", "%s")' % (item['title'], item['detail_url'])
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


class RedisPipeline(object):
    """
    将解析到的数据存储到redis中
    """
    conn = None

    def open_spider(self, spider):
        self.conn = redis.Redis(host='192.168.1.197', port=6379)
        print(self.conn)

    def process_item(self, item, spider):
        dic = {
            'title': item['title'],
            'detail_url': item['detail_url']
        }
        import json
        self.conn.lpush('xiaohua', json.dumps(dic))
        return item

    def close_spider(self, spider):
        pass
