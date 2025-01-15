import requests
from bs4 import BeautifulSoup

#agente
encabezados = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

#url semilla
url = "https://stackoverflow.com/questions"

respuesta = requests.get(url, headers=encabezados)#devuelve la respuesta

soup = BeautifulSoup(respuesta.text)

contenedor_de_preguntas = soup.find(id="questions") #devuleve un elemento
lista_de_preguntas = contenedor_de_preguntas.findAll("div", class_="s-post-summary") #devuelve todos los elementos

for pregunta in lista_de_preguntas:
    # texto_pregunta = pregunta.find("h3").text 
    # descripcion_pregunta = pregunta.find(class_="s-post-summary--content-excerpt").text #busqueda con una clase

    elemento_texto_pregunta = pregunta.find("h3")
    texto_pregunta = elemento_texto_pregunta.text

    descripcion_pregunta = elemento_texto_pregunta.find_next_sibling("div").text #busqueda del siguiente elemento

    descripcion_pregunta = descripcion_pregunta.replace("\n", "").replace("\r", "").strip()
    print(texto_pregunta)
    print(descripcion_pregunta,"\n")
