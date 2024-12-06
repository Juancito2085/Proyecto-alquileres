import scrapy


class AlquileresRosarioSpider(scrapy.Spider):
    name = "alquileres_rosario"
    allowed_domains = ["argenprop.com.ar"]
    start_urls = ["https://www.argenprop.com/departamentos/alquiler/rosario-santa-fe"]

    
    def parse(self, response):
        inmuebles = response.css(".listing__item")
        for inmueble in inmuebles:
            yield {
                "precio": inmueble.css('.card__price').get().split(' ')[27].replace('\n', ''),
                "moneda": inmueble.css(".card__currency::text").get(),
                "expensas": inmueble.css(".card__expenses::text").get().split(';')[1].replace('\nexpensas','').strip(),
                "ubicación": inmueble.css("span::text").get(),
                "zona": inmueble.css("span::text").get(),
                "url": inmueble.css("a::attr(href)").get(),
            }
        pass
