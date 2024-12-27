# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InmueblesCaracteristicas(scrapy.Item):
    precio = scrapy.Field()
    expensas = scrapy.Field()
    direccion = scrapy.Field()
    latitud = scrapy.Field()
    longitud = scrapy.Field()
    ambientes = scrapy.Field()
    dormitorios = scrapy.Field()
    baños = scrapy.Field()
    superficie_cubierta = scrapy.Field()
    antiguedad = scrapy.Field()
    orientacion = scrapy.Field()
    estado = scrapy.Field()
    disposicion = scrapy.Field()
    tipo = scrapy.Field()

