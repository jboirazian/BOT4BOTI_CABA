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


DNI=[39911811, 39911839, 39911863, 39911886, 39911888, 39911900, 39911902,
 39911920, 39911945, 39911981, 39912019, 39912033, 39912052, 39912064,
 39912070, 39912118, 39912131, 39912143, 39912151, 39912169, 39912204,
 39912229, 39912237, 39912277, 39912305, 39912324, 39912343, 39912344,
 39912361, 39912395, 39912421, 39912450, 39912452, 39912459, 39912469,
 39912497, 39912510, 39912523, 39912569, 39912604, 39912630, 39912634,
 39912707, 39912723, 39912725, 39912727, 39912743, 39912751, 39912784,
 39912825, 39912990, 39913046, 39913115, 39913131, 39913143, 39913192,
 39913231, 39913274, 39913287, 39913293, 39913366, 39913372, 39913404,
 39913408, 39913487, 39913514, 39913523, 39913548, 39913552, 39913660,
 39913704, 39913713, 39913743, 39913746, 39913754, 39913835, 39913861,
 39913884, 39913905, 39913947, 39914017, 39914031, 39914053, 39914061,
 39914078, 39914090, 39914181, 39914217, 39914263, 39914282, 39914294,
 39914322, 39914346, 39914407, 39914447, 39914523, 39914546, 39914547,
 39914566, 39914583]
 
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
	
	
	
	
	
	
