import scrapy


class InmuebleSpider(scrapy.Spider):
    name = "inmueble"
    allowed_domains = ["zonaprop.com.ar"]
    start_urls = ["https://zonaprop.com.ar"]

    def parse(self, response):
        pass
