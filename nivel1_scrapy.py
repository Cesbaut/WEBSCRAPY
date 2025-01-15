from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader #carga mis items


# scrapy runspider .\nivel1_scrapy.py -o video.csv 

class Pregunta(Item):
    id = Field()
    pregunta = Field()
    #descripcion = Field()

class StackOverFlowSpider(Spider):
    name = "MiPrimerSpider" #nombre
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }  

    start_urls = ["https://stackoverflow.com/questions"] #url


    def parse(self, response): #funcion para el parceo
        sel = Selector(response) #sirve par ahacer consultas a la pagina
        preguntas = sel.xpath("//div[@id='questions']//div[contains(@class,'s-post-summary')]") 


        for pregunta in preguntas:
            item = ItemLoader(Pregunta(), pregunta)
            item.add_xpath("pregunta", ".//h3/a/text()" ) #que propiedad llenar, con cual xpath cargare la propiedad  
            #item.add_xpath("descripcion",".//div[@class='s-post-summary--content-excerpt']/text()" ) #ponemos un punto por posicion relativa
            item.add_value("id",1) #sirve para llenar una propiedad con un valor directamente

            yield item.load_item() #return que manda a un archivo la informacion de mis items


