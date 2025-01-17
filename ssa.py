import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re



    
    





opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
opts.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=opts)

driver.get('https://www.ssa.ingenieria.unam.mx/horarios.html') #url

clave =  driver.find_element("xpath", "//input[@id='clave']") #obtencion de botones
clave.send_keys("1414")
boton =  driver.find_element("xpath", "//button[@id='buscar']")
boton.click()

clases = driver.find_elements("xpath", '//tbody') #se obtienen las clases
clases = clases[1:]

for clase in clases:
    if (clase.text == ""):
        break
    datos = clase.find_elements("xpath", './tr/td')
    texto_celdas = [dato.text for dato in datos]
    texto_celdas[2] = re.sub(r'\n.*', '', texto_celdas[2]).strip()


    print(texto_celdas)


