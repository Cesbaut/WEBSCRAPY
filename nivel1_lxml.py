import requests
from lxml import html

encabezados = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

url = "https://www.wikipedia.org/"

respuesta = requests.get(url, headers=encabezados)

parser = html.fromstring(respuesta.text)

# ingles = parser.get_element_by_id("js-link-box-en") #encuentra los elementos por su identificador

# print(ingles.text_content())

# idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()") #encuentra elementos por el xpath

# for idioma in idiomas:
#     print(idioma)

idiomas = parser.find_class('central-featured-lang') #encuentra elemento por clase
for idioma in idiomas:
    print(idioma.text_content())