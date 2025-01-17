import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re



    
def inicio(numero):    





    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
    opts.add_argument("--disable-search-engine-choice-screen")
    opts.add_argument("--headless")  # Modo sin interfaz gráfica
    opts.add_argument("--disable-gpu")  # Deshabilitar uso de GPU (a veces necesario en headless)
    opts.add_argument("--window-size=1920,1080")  # Tamaño de ventana (opcional)

    driver = webdriver.Chrome(options=opts)

    driver.get('https://www.ssa.ingenieria.unam.mx/horarios.html') #url

    clave =  driver.find_element("xpath", "//input[@id='clave']") #obtencion de botones
    clave.send_keys(numero)
    boton =  driver.find_element("xpath", "//button[@id='buscar']")
    boton.click()

    clases = driver.find_elements("xpath", '//tbody') #se obtienen las clases
    clases = clases[1:]
    lista=[]
    for clase in clases:
        if (clase.text == ""):
            break
        try:
            datos = clase.find_elements("xpath", './tr/td')
            diccionario={}
            texto_celdas = [dato.text for dato in datos]
            texto_celdas[2] = re.sub(r'\n.*', '', texto_celdas[2]).strip()
            diccionario["clave"] = texto_celdas[0]
            diccionario["grupo"] = texto_celdas[1]
            diccionario["nombre"] = texto_celdas[2]
            diccionario["tipo"] = texto_celdas[3]
            diccionario["horas"] = texto_celdas[4]
            diccionario["dias"] = texto_celdas[5]
            diccionario["cupo"] = texto_celdas[6]
            lista.append(diccionario)
            print(diccionario)
        except:
            break


inicio("1414")