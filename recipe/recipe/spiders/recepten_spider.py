from scrapy import Spider

class ReceptenSpider(Spider):
    name, start_urls = 'recepten', ['http://www.recepten.se/artiklar/veckomeny.html'] #http://www.recepten.se/artiklar/veckomeny.html
    allowed_domains = ["recepten.se"]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        #return [Recipe(title=e.extract()) for e in response.css("a::text")]