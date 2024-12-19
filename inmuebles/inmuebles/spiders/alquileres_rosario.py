import scrapy


class AlquileresRosarioSpider(scrapy.Spider):
    name = "alquileres_rosario"
    allowed_domains = ["argenprop.com"]
    start_urls = ["https://www.argenprop.com/departamentos/alquiler/rosario-santa-fe"]

    
    def parse(self, response):


        inmuebles = response.css(".card")
        for inmueble in inmuebles:
            expenses_text=inmueble.css(".card__expenses::text").get()
            if expenses_text != None:
                expensas = expenses_text.split(';')[1].replace('\nexpensas','').strip()
                expensas = expensas.replace('"','')
            else:
                expensas = 0

            yield {
                "precio": inmueble.css('.card__price').get().split(' ')[27].replace('\n', ''),
                "moneda": inmueble.css(".card__currency::text").get(),
                "expensas": expensas,
                "ubicación": inmueble.css('p.card__address::text').get().replace('\n','').strip(),
                "url": inmueble.css("a::attr(href)").get(),
            }
        pagina_siguiente = response.css('[rel="next"]::attr(href)').get()
        
        if pagina_siguiente:
            
            url_pagina_siguiente = "https://www.argenprop.com" + pagina_siguiente
            print(url_pagina_siguiente)
            yield response.follow(url_pagina_siguiente, callback=self.parse)

