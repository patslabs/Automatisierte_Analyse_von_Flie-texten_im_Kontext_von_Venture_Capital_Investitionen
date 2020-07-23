README SCRAPY APPLICATION

Just don't do it.
The application and the results produced by this scrapy code are not usefull. If you still want to find out more about it, try it on your own and use
the information provided on their website: https://scrapy.org

***Prerequisites:***
Python 3
Python GUI of your choice (My choice: https://www.jetbrains.com/pycharm/)
Scrapy Default APP (http://docs.scrapy.org/en/latest/intro/tutorial.html)


***Getting started:***
1. Check the prerequisites and if you realy have that much time to waste.
2. Follow the instruction on (http://docs.scrapy.org/en/latest/intro/tutorial.html)

The code of my spider(Other than that I didn't realy change much:
 def parse(self, response):
        self.start_time = time.time()
        self.counter = 0


        for quote in response.xpath('//div'):
            yield {
                "text": quote.xpath("//h1/text()").getall(),
                "texth2": quote.xpath("//h2/text()").getall(),
            }
        for href in response.xpath('//a/@href'):
            yield response.follow(href, self.parse)