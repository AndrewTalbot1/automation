import scrapy

class BookSpider(scrapy.Spider):
    name = "book_info"
    start_urls = [
        'http://books.toscrape.com/',
    ]

    custom_settings = {
        'DEPTH_LIMIT' : 0,
    }

    def parse(self, response):
        for book_info in response.css('li.col-xs-6'):
            yield{
                "Title": book_info.css('h3 a::text').get(),
                "Price" : book_info.css('p.price_color::text').get(),
                "Rating" : book_info.xpath(
                    './/*[contains(concat( " ", @class, " " ), concat( " ", "star-rating", " " ))]')
                    .extract_first()
                    .replace('star-rating',"").replace('\n', '')
                    .replace(' <i class="icon-star"></i>','')
                    .replace('<p class=','')
                    .replace('</p>',''),
                "In Stock" : book_info.xpath(
                    './/*[contains(concat( " ", @class, " " ), concat( " ", "availability", " " ))]')
                    .extract_first()
                    .replace('<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        ','')
                    .replace('\n    \n</p>',''),
            }
        
        next_page = response.xpath('.//*[contains(concat( " ", @class, " " ), concat( " ", "next", " " ))]//a').attrib['href']

        yield response.follow(next_page, callback=self.parse)