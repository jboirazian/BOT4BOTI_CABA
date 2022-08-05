from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.command import Command
import os
import time
from bs4 import BeautifulSoup
import re

options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe",options=options)
nombre_Whatsapp_del_bot="Buenos Aires Ciudad"

def enviar_mensaje(texto):
	link_escribir_mensaje.send_keys(texto)
	link_escribir_mensaje.send_keys(Keys.RETURN)
	return

def vacuna2(DNI , MENSAJE):
	t1="A ver, dame unos segundos…"
	t2="-19"
	t3="Uy"
	t4="Si ya te anotaste, lo más seguro"
	t5="Ya "
	t6="Componente"
	MENSAJE=MENSAJE.replace('\n'," ")
	result = re.search('%s(.*)%s' % (t1, t2), MENSAJE)
	if result is None:
		result=re.search('%s(.*)%s' % (t3, t4), MENSAJE)
		if result is None:
			result=re.search('%s(.*)%s' % (t5, t6), MENSAJE)
			if result is None:
				result="ERROR"
	return str(result.group(1))


print("INICIANDO SCRAPPING :) ")
driver.get("https://web.whatsapp.com/")
input("Escanea el codigo QR y luego presioná ENTER para comenzar....")
link_contactos=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')


time.sleep(2)### BUSCAMOS EL NUMERO DE TELEFONO EN LA AGENDA Y LO SELECCIONAMOS
link_contactos.send_keys(nombre_Whatsapp_del_bot)
time.sleep(1)
link_contactos.send_keys(Keys.RETURN) 


DNI=[]### Enter all the DNIs
 
GEN="M" ### M o F
i=0
f= open("vacunacion.txt","r+")
link_escribir_mensaje=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
while i!=len(DNI)-1:
	time.sleep(1)
	enviar_mensaje("Menu")### ENVIAMOS EL PRIMER MENSAJE PARA ARRANCAR
	time.sleep(1)
	enviar_mensaje("C") ### VACUNA COVID-19
	time.sleep(1)
	enviar_mensaje("C") ### ESTOY EN EL PADRON ?
	time.sleep(1)
	enviar_mensaje("A") ### DNI
	time.sleep(1)
	enviar_mensaje(str(DNI[i])) ### INGRESO NUMERO DE DNI
	time.sleep(1)
	enviar_mensaje(GEN) ### INGRESO GENERO
	time.sleep(10)
	content = driver.page_source
	soup = BeautifulSoup(content,'html.parser')
	texto_del_bot=str(soup.get_text())
	resultado=vacuna2(DNI[i],texto_del_bot)
	f.write(str(DNI[i])+";"+ resultado + ";"+'\n')
	print(resultado)
	time.sleep(5)
	i+=1
f.close()
	
	
	
	
	
	
