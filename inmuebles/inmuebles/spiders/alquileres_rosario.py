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
            'direccion':response.css('h2.titlebar__address::text').get(),
            'latitud':response.css('[data-latitude]::attr(data-latitude)').get(),
            'longitud':response.css('[data-longitude]::attr(data-longitude)').get(),
            'ambientes':response.css('li[title="Ambientes"] p::text').get().split()[0],
            'dormitorios':response.css('li[title="Dormitorios"] p::text').get().split()[0],
            'baños':response.css('li[title="Baños"] p::text').get().split()[0],
            'superficie cubierta':response.css('li[title="Sup. cubierta"] p::text').get().split()[0],
            'antiguedad':response.css('li[title="Antiguedad"] p::text').get(),
            'orientacion':response.css('li[title="Orientación"] p::text').get(),
            'estado':response.css('li[title="Estado"] p::text').get(),
            'disposicion':response.css('li[title="Disposición"] p::text').get(),
            # 'tipo':
        }