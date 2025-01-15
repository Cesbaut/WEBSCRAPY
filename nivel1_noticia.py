from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

from bs4 import BeautifulSoup

from scrapy.crawler import CrawlerProcess #para ejecucion sin consola


class Noticia(Item):
    titular = Field()
    descripcion = Field()

class ElUniversoSpider(Spider): #Siempre debe heredar de spaider
    name = "MiSegundoSpider"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }  

    start_urls = ["https://www.eluniverso.com/deportes/"] 

    def parse(self, response):
        # sel = Selector(response)
        # noticias = sel.xpath("//li[contains(@class, 'relative')]/div[contains(@class, 'card')]")
        # for noticia in noticias:
        #     item = ItemLoader(Noticia(),noticia)
        #     item.add_xpath("titular", ".//h2/a/text()")
        #     item.add_xpath("descripcion", ".//p/text()")

        #     yield item.load_item()

        soup = BeautifulSoup(response.body)
        contenedor_noticias = soup.find_all("li", class_="relative")

        for contenedor in contenedor_noticias:
            noticias = contenedor.find_all("div",class_="card", recursive=False) #Recursive : la busqueda se hara en los hijos directos o en cualquier hijo
            for noticia in noticias:
                item = ItemLoader(Noticia(), response.body)

                titular = noticia.find("h2")

                descripcion = noticia.find("p")

                if(titular != None):
                    titular = titular.text
                else:
                    titular = "N/A"
                if (descripcion != None):
                    descripcion = descripcion.text
                else:
                    descripcion = "N/A"

           
                item.add_value("titular", titular)
                item.add_value("descripcion", descripcion)

                yield item.load_item()



#Ejecucion sin consola
process = CrawlerProcess({
    'FEED_FORMAT': 'json',
    'FEED_URI': 'datos_de_salida_3.json'
})

process.crawl(ElUniversoSpider)
process.start()