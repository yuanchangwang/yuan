import json
import os

import requests
from bs4 import BeautifulSoup


# - 1. 爬取任意城市的肯德基餐厅的位置信息
"""
# 1.指定URL
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

# 2.指定请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 chrome-extension'
}

city = input('请输入你要爬取的城市名称？>>>')

all_data_list = []
for i in range(1, 11):
    data = {
        'cname': '',
        'pid': '',
        'keyword': city,
        'pageIndex': i,
        'pageSize': '10'
    }

    # 3.发送请求
    json_obj = requests.post(url=url, headers=headers, data=data).json()

   # 4.获取响应数据
    for data in json_obj['Table1']:
        all_data_list.append(data)

print(all_data_list)
# 5.存储数据
with open('kfc.txt', 'w', encoding='utf-8') as f:
    for data in all_data_list:
        json.dump(data, f, ensure_ascii=False)
        f.write('\n')
"""

# - 3. 使用bs4爬取史书典籍上面的所有文章内容http://www.shicimingju.com/book/index.html
# 1.指定URL
url = 'http://www.shicimingju.com/book/index.html'
# 2.指定请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 chrome-extension'
}
# 3.发送请求
page_text = requests.get(url=url, headers=headers).text

# 4.解析所有的书籍
soup = BeautifulSoup(page_text, 'lxml')
book_list = soup.select('.bookmark-list li')

# print(book_list)

# 创建一个books目录
if not os.path.exists('./books'):
    os.mkdir('./books')

for book in book_list:
    # 每本书的URL
    book_url = 'http://www.shicimingju.com' + book.h2.a['href']
    # 向每本书发送请求
    page_text = requests.get(url=book_url, headers=headers).text
    # 解析每本书的所有章节
    soup = BeautifulSoup(page_text, 'lxml')
    chapter_list = soup.select('.book-mulu li')

    book_title = './books/' + book.h2.text + '.txt'
    # 保存书籍数据
    with open(book_title, 'w', encoding='utf-8') as f:
        for chapter in chapter_list:
            # 获取到章节名
            chapter_title = chapter.a.string
            # 每一章的URL
            detail_url = 'http://www.shicimingju.com' + chapter.a['href']
            # 向详情页发送请求，获取到详情页的文本数据
            detail_page_text = requests.get(url=detail_url, headers=headers).text
            # 解析所有的文本信息
            detail_soup = BeautifulSoup(detail_page_text, 'lxml')
            div_tag = detail_soup.find('div', class_='chapter_content')
            detail_text = div_tag.get_text()
            # 存储数据
            f.write(chapter_title + ':' + detail_text + '\n')
    print(book_title + '完')
