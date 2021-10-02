import scrapy
from scrapy import Request
import scraper_helper as sh
from scrapy.selector import Selector
#from ..items import AmazonItem

review_url = 'https://www.amazon.com/product-reviews/{}'
asin_list = ['B07PS737QQ']
# airpods : B07PYLT6DN

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    
    def start_requests(self):
        for asin in asin_list:
            url = review_url.format(asin)
            yield scrapy.Request(url)

    def parse(self, response):
        print("I am in parse")
        for review in response.css('[data-hook = "review"]'):
            item = {
                #'Product_name': review.xpath('normalize-space(.//*[@data-hook = "product-link"] ::text').get(),
                'review_title': review.css('[data-hook = "review-title"] span ::text').get(),
                'product_review': review.xpath('normalize-space(.//*[@data-hook="review-body"]/span/text())').get(),
                #'product_review': review.css('[data-hook = "review-body"] span ::text').get(),
                'product_rating': review.css('[data-hook = "review-star-rating"] ::text').get(),
                'reviewer': review.css('.a-profile-name ::text').get()
            }
            yield item
            
        next_page = review.xpath('//a[text() = "Next page"]/@href').get()    
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
       
            
        
         
    

        
