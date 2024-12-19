import scrapy


class AlquileresRosarioSpider(scrapy.Spider):
    name = "alquileres_rosario"
    allowed_domains = ["argenprop.com.ar"]
    start_urls = ["https://www.argenprop.com/departamentos/alquiler/rosario-santa-fe"]

    
    def parse(self, response):
        inmuebles = response.css(".card")
        for inmueble in inmuebles:
            expenses_text=inmueble.css(".card__expenses::text").get()
            if expenses_text != None:
                expensas = expenses_text.split(';')[1].replace('\nexpensas','').strip()
                expensas=expensas.replace('"','')
                expensas=float(expensas.replace('.','').replace(',','.'))
            else:
                expensas = 0

            yield {
                "precio": inmueble.css('.card__price').get().split(' ')[27].replace('\n', ''),
                "moneda": inmueble.css(".card__currency::text").get(),
                "expensas": expensas,
                "ubicación": inmueble.css("span::text").get(),
                "zona": inmueble.css("span::text").get(),
                "url": inmueble.css("a::attr(href)").get(),
            }
        pass
