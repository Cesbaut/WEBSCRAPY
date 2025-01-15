import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/news"

#agente
encabezados = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

respuesta = requests.get(url, headers=encabezados)

soup = BeautifulSoup(respuesta.text)

lista_de_noticias = soup.find_all("tr", class_="athing")

for noticia in lista_de_noticias:
    titulo = noticia.find("span", class_="titleline").text
    url = noticia.find("span", class_="titleline").find("a").get("href")#con get entramos a los atributos

    metadata = noticia.find_next_sibling()

    score = 0
    comentarios=0


    try:
        score_tmp = metadata.find("span", class_="score").text
        score_tmp = score_tmp.replace("points","").strip()
        score = int(score_tmp)
    except:
        print("No hay puntos")

    try:
        comentarios_tmp = metadata.find("span", attrs={"class":"subline"}).text #atributos busca los atibutos que buscamos
        comentarios_tmp = comentarios_tmp.split("|")[-1]
        comentarios_tmp = comentarios_tmp.replace("comments","").strip()
        comentarios = int(comentarios_tmp)
    except:
        print("no hay comentarios")


    print(titulo)
    print(score)
    print(comentarios)
    print(url,"\n")


