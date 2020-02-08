import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import LinkSpiderItem
class LinkSpider(CrawlSpider):
    name = "list of links"
    allowed_domains = ['books.toscrape.com',]
    start_urls =[
        'http://books.toscrape.com/',
    ]
    rules = (Rule(LinkExtractor(), callback='parse_links', follow=True), )

    custom_settings = {
        "DEPTH_LIMIT" : 0,
    }


    def parse_links(self, response):
        #self.logger.info('Hi, this is an item page! %s', response.url)
        item = LinkSpiderItem()
        item['urls'] = response.url
        return item
        