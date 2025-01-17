import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Asi podemos setear el user-agent en selenium
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
# Agregar a todos sus scripts de selenium para que no aparezca la ventana de seleccionar navegador por defecto: (desde agosto 2024)
opts.add_argument("--disable-search-engine-choice-screen")

# Instancio el driver de selenium que va a controlar el navegador
# A partir de este objeto voy a realizar el web scraping e interacciones
driver = webdriver.Chrome(options=opts)

driver.get('https://www.olx.in/')

boton =  driver.find_element("xpath", "//button[@data-aut-id='btnLoadMore']")

boton2 =  driver.find_element("xpath", "//input[@data-aut-id='searchBox']")

boton2.send_keys("Texto que quiero escribir")


for i in range(1):
    try:
        boton.click()
        sleep(random.uniform(8,10))
        boton =  driver.find_element("xpath", "//button[@data-aut-id='btnLoadMore']")
        print("se apreto")
    except:
        break

autos = driver.find_elements("xpath", '//li[@data-aut-id="itemBox3"]')

i=0
for auto in autos:
    i=i+1
    print(i)
    precio = auto.find_element("xpath", ".//span[@data-aut-id='itemPrice']").text
    print(precio)
    descripcion =  auto.find_element("xpath", './/span[@data-aut-id="itemTitle"]').text
    print(descripcion)

