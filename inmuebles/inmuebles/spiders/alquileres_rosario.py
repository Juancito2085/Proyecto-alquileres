import scrapy
from inmuebles.items import InmueblesCaracteristicas
from inmuebles.itemloaders import InmueblesCaracteristicasLoader

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
        pagina_siguiente = response.css('[rel="next"]::attr(href)').get()
        
        if pagina_siguiente:
            
            url_pagina_siguiente = "https://www.argenprop.com" + pagina_siguiente
            print(url_pagina_siguiente)
            yield response.follow(url_pagina_siguiente, callback=self.parse)

    def pag_inmueble_parse(self, response):

        # inmuebles_caracteristicas.add_css( = InmueblesCaracteristicas()
        inmueble = InmueblesCaracteristicasLoader(item=inmuebles_caracteristicas.add_css(, response=response)
        # texto_expensas = response.css('p.titlebar__expenses::text').get()
        # if texto_expensas:
        #     expensas = texto_expensas.split()[1]
        # else:
        #     expensas = 'No tiene'
        
        # ambientes = response.css('li[title="Ambientes"] p::text').get()
        # if ambientes:
        #     ambientes = ambientes.split()[0]
        # else:
        #     ambientes = 'Sin datos'
        
        # dormitorios = response.css('li[title="Dormitorios"] p::text').get()
        # if dormitorios:
        #     dormitorios = dormitorios.split()[0]
        # else:
        #     dormitorios = 'Sin datos'
        
        # baños = response.css('li[title="Baños"] p::text').get()
        # if baños:
        #     baños = baños.split()[0]
        # else:
        #     baños = 'Sin datos'

        # superficie_cubierta = response.css('li[title="Sup. cubierta"] p::text').get()
        # if superficie_cubierta:
        #     superficie_cubierta = superficie_cubierta.split()[0]
        # else:
        #     superficie_cubierta = 'Sin datos'

        # antiguedad = response.css('li[title="Antiguedad"] p::text').get()
        # if antiguedad:
        #     antiguedad = antiguedad
        # else:
        #     antiguedad = 'Sin datos'

        # orientacion = response.css('li[title="Orientación"] p::text').get()
        # if orientacion:
        #     orientacion = orientacion
        # else:
        #     orientacion = 'Sin datos'

        # estado = response.css('li[title="Estado"] p::text').get()
        # if estado:
        #     estado = estado
        # else:
        #     estado = 'Sin datos'

        # disposicion = response.css('li[title="Disposición"] p::text').get()
        # if disposicion:
        #     disposicion = disposicion
        # else:
        #     disposicion = 'Sin datos'

        # tipo = response.css('ul.property-main-features li:first-child p::text').get()
        # if tipo:
        #     tipo = tipo
        # else:  
        #     tipo = 'Sin datos'

        inmueble.add_css('precio', response.css('p.titlebar__price::text').get().replace('\n','').strip()),
        inmuebles_caracteristicas.add_css('expensas', expensas),
        inmuebles_caracteristicas.add_css('direccion', 'h2.titlebar__address::text'),
        inmuebles_caracteristicas.add_css('latitud', '[data-latitude]::attr(data-latitude)'),
        inmuebles_caracteristicas.add_css('longitud','[data-longitude]::attr(data-longitude)'),
        inmuebles_caracteristicas.add_css('ambientes', ambientes),
        inmuebles_caracteristicas.add_css('dormitorios', dormitorios),
        inmuebles_caracteristicas.add_css('baños', baños),
        inmuebles_caracteristicas.add_css('superficie_cubierta', superficie_cubierta),
        inmuebles_caracteristicas.add_css('antiguedad', antiguedad),
        inmuebles_caracteristicas.add_css('orientacion', orientacion),
        inmuebles_caracteristicas.add_css('estado', estado),
        inmuebles_caracteristicas.add_css('disposicion', disposicion),
        inmuebles_caracteristicas.add_css('tipo', tipo)

        yield inmuebles_caracteristicas.load_item()
            