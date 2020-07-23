import scrapy
import time

class QuotesSpider(scrapy.Spider):
    name = "NAME"
    start_urls = [
        #'https://www.leggmason.com'
        #'https://www.kayak.de/?ispredir=true'
        #'https://www.yelp.de/frankfurt-am-main'
        #'https://medium.com/'
        #'https://medium.com/s/story/the-insane-structure-of-high-school-762fea58fe62'
        #'https://medium.com/s/story/a-weak-president-can-still-be-a-dangerous-one-aaf0ec469ca9'
        #'https://medium.com/s/story/farming-is-polarized-agtech-is-a-bridge-231b35102098'
        #'https://www.klarna.com/de/'
        #'https://brighter.ai'
        'https://www.uber.com/business/'
        ]

    def parse(self, response):
        self.start_time = time.time()
        self.counter = 0
        # for quote in response.xpath('//div[@class="section-content"]'):
        #     #self.counter += 1
        #     yield {
        #         "text": quote.xpath("//p/text()").getall(),
        #         "author": quote.xpath("//h3[@class='ui-h2']/text()"),
        #     }

        for quote in response.xpath('//div'):
            yield {
                "text": quote.xpath("//h1/text()").getall(),
                "texth2": quote.xpath("//h2/text()").getall(),
                #"author": quote.xpath("//h3[@class='ui-h2']/text()"),
            }


        #
        #if self.start_time > (time.time() + 5):
        #    raise CloseSpider("bandwith_exceeded")
        #if self.counter > 4:
        #    raise CloseSpider("counter error")

        #next_page = response.xpath('//div[@class="recommendation"]//a/@href').get()
        #for href in response.xpath('//div[@class="recommendation"]//a/@href'):
        #    yield response.follow(href, self.parse)

        #for href in response.xpath('//div[@class=elevate-container]//a/@href'):
        #    yield response.follow(href, self.parse)

        for href in response.xpath('//a/@href'):
            yield response.follow(href, self.parse)
            #Follow it all
#'https://www.gruenderszene.de/technologie/macht-samsung-die-gleichen-fehler-wie-apple',
#        'https://www.gruenderszene.de/gs-connect/exist/esports-deutschland-vorurteile-exist-2015-3564',
