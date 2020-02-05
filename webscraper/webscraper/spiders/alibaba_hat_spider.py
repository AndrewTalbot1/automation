import scrapy

class HatsSpider(scrapy.Spider):
    name = "hat_list"
    start_urls = [
        'https://www.alibaba.com/products/hats/CID32708.html?spm=a2700.galleryofferlist.0.0.2d7546c4jCXuac&IndexArea=product_en',
    ]

    custom_settings = {
        "DEPTH_LIMIT": 1,
        "ROBOTSTXT_OBEY": False,
        "AUTOTHROTTLE_ENABLE": True,
        "AUTOTHROTTLE_START_DELAY": 5.0,
    }
    def parse(self, response):
        for hat_list in response.css('div.organic-gallery-offer-outter'):
            yield{
                "Title": hat_list.css('p.organic-gallery-title__content::text').get(),
                "Price": hat_list.css('p.gallery-offer-price span::text').get(),
                "Min Order": hat_list.css('p.gallery-offer-minorder span::text').get(),
                "Country": hat_list.css("div.organic-gallery-offer-section__seller-tags span::text").get(),
                "Years In Business": hat_list.css("div.organic-gallery-offer-section__seller-tags span.seller-tag__year::text").get(),
                "Response Rate": hat_list.css('div.organic-gallery-offer-section__reviews span::text').get(),
                "Review Score": hat_list.css('div.organic-gallery-offer-section__reviews span.seb-supplier-review__score::text').get(),
                "Contact Link": response.urljoin(hat_list.css('div.organic-gallery-offer-section__contact a::attr(href)').get()),
            }
        #response.css('div.organic-gallery-offer-section__contact a::attr(href)').get()
        