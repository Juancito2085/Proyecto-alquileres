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
        texto_expensas = response.css('p.titlebar__expenses::text').get()
        if texto_expensas:
            expensas = texto_expensas.split()[1]
        else:
            expensas = 'No tiene'
        yield {
            'precio':response.css('p.titlebar__price::text').get().replace('\n','').strip(),
            'expensas':expensas,
            'direccion':response.css('h2.titlebar__address::text').get()
            latitud
        }