import scrapy


class AuthorSpider(scrapy.Spider):
    name = "author_links"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]
    # Limits the amount of pages it will crawl the value 
    # 0 doesn't have a limit
    custom_settings = {
        'DEPTH_LIMIT': 1,
        'ROBOTSTXT_OBEY': False,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 5.0,
        'AUTOTHROTTLE_MAX_DELAY': 60.0,
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 0.5,

    }
    
    def parse(self, response):
        for author_links in response.css('div.quote'):
            yield{
                "author links": response.urljoin(author_links.css('a::attr(href)').get()),
            }

        next_page = response.css('li.next a::attr(href)').get()
        #if next_page is not None:
        yield response.follow(next_page, callback=self.parse)

#scrapy crawl <spidername> -o <filename>.json
