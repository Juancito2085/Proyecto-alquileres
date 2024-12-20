import scrapy


class AlquileresRosarioSpider(scrapy.Spider):
    name = "alquileres_rosario"
    allowed_domains = ["argenprop.com"]
    start_urls = ["https://www.argenprop.com/departamentos/alquiler/rosario-santa-fe"]

    
    def parse(self, response):


        inmuebles = response.css(".card")
        for inmueble in inmuebles:
            url_relativa = inmueble.css("a::attr(href)").get()
            url_inmueble = 'https://www.argenprop.com' + url_relativa
            print(url_inmueble)
            yield response.follow(url_inmueble, callback=self.pag_inmueble_parse)
#        pagina_siguiente = response.css('[rel="next"]::attr(href)').get()
        
 #       if pagina_siguiente:
            
  #          url_pagina_siguiente = "https://www.argenprop.com" + pagina_siguiente
   #         print(url_pagina_siguiente)
    #        yield response.follow(url_pagina_siguiente, callback=self.parse)

    def pag_inmueble_parse(self, response):
        
        yield {
            'precio':response.css('p.titlebar__price::text').get().replace('\n','').strip(),

        }