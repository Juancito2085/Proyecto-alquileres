from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst

class InmueblesCaracteristicasLoader(ItemLoader):
    default_output_processor = TakeFirst()
    pass