import scrapy
from laravel_test.items import LaravelTestItem


class LaravelScrapingSpider(scrapy.Spider):
    name = "laravel_scraping"
    allowed_domains = ["10.146.221.37:8081/get_title.html"]
    start_urls = ["http://10.146.221.37:8081/get_title.html"]

    def parse(self, response):
        '''
        print(response.css('title'))
        print(response.css('title ::text'))
        '''
        title_element = response.xpath('//title')
        
        # タイトル要素からテキストを取得
        title_text = title_element.get()

        # タイトルテキストを表示
        print('ページのタイトル:', title_text)