import scrapy
from ..items import QouteItem

class Qoute(scrapy.Spider):
    name = 'qoutes'
    start_urls = [
        'https://quotes.toscrape.com'
    ]

    def parse(self,response):
        
        items = QouteItem()

        all_div_qoutes = response.css('div.quote')

        for qoutes in all_div_qoutes:
            title = qoutes.css('span.text::text').extract_first()
            author = qoutes.css('.author::text').extract_first()
            tags = qoutes.css('.tag::text').extract()
            
            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            
            yield items

        next_page = response.css('li.next a::attr(href)').get()
        
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)