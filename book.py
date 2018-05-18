# # coding=utf-8
import requests
from lxml import etree

class Book():
    def __init__(self):
        self.url='http://www.cuiweijuxing.com/files/article/html/0/833/index.html'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64)' 'AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/63.0.3239.84 Safari/537.36','X-CSRFToken':'9303a1f4b25e8f2f68d89b1d0e9cf615','Referer':'http://neihanshequ.com/bar/1/','Cookie':'uuid="w:99d7c4dc60eb4ae09556c6bc9dc6d253"; tt_webid=6529659478042854919; csrftoken=13753cb398583c33da5be8bf0f7727f7; _ga=GA1.2.1382869523.1520304821; _gid=GA1.2.1200588661.1520422263'}

    def parse_url(self):
        response = requests.get(self.url, headers=self.headers)
        html = response.content.decode('gbk')
        return html

    def get_chapter(self,html):
        data = etree.HTML(html)
        book_name = data.xpath('//div[@style="text-align:center;"]/span[@style="font-size:20px;font-weight:bold;color:#f27622;"]/text()')
        # chapter_list = data.xpath('//li[@class="chapter"]')
        chapter_list=data.xpath('//div[text()="《万古龙帝》正文"]/parent::div//li[@class="chapter"]')
        # chapter_list.reverse()
        for chapter in chapter_list:
            href = chapter.xpath('./a/@href')[0]
            chapter_name = chapter.xpath('./a/text()')[0]
            content = self.get_chapter_content(href,chapter_name,book_name)
            print(content)

    def write_book(self,content,chapter_name,book_name):
        with open(book_name,'w') as f:
            f.write(content)


    def get_chapter_content(self,url,chapter_name,book_name):
        response = requests.get(url, headers=self.headers)
        html = response.content.decode('gbk')
        data = etree.HTML(html)
        content = data.xpath('//div[@class="content"]/text()')
        for data in content:
            self.write_book(data,chapter_name,book_name[0])


    def run(self):
        html=self.parse_url()
        self.get_chapter(html)
if __name__ == '__main__':
    spider=Book()
    spider.run()
#
#
#
#
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64)' 'AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/63.0.3239.84 Safari/537.36','X-CSRFToken':'9303a1f4b25e8f2f68d89b1d0e9cf615','Referer':'http://neihanshequ.com/bar/1/','Cookie':'uuid="w:99d7c4dc60eb4ae09556c6bc9dc6d253"; tt_webid=6529659478042854919; csrftoken=13753cb398583c33da5be8bf0f7727f7; _ga=GA1.2.1382869523.1520304821; _gid=GA1.2.1200588661.1520422263'}
# response = requests.get(url, headers=headers)
# html = response.content.decode('gbk')