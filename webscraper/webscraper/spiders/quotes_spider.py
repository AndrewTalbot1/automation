import scrapy


class AuthorSpider(scrapy.Spider):
    name = "author_links"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    
    def parse(self, response):
        for author_links in response.css('div.quote'):
            yield{
                "author links": response.urljoin(author_links.css('a::attr(href)').get()),
            }
#scrapy crawl <spidername> -o <filename>.xml
