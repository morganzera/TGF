import time
from password import nome,senha
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
tabela_data = pd.read_excel(r"C:\Users\pc\Documents\PIBIC_PY\Pibic\Data_fermi.xlsx")

print("#### Iniciando o BOT ####")
for i in range (25):
# Data do evento
    print("## i = " + str(i) + " ##")
    print("########################")
    data = str(tabela_data['D'][i])
    data = data.replace(" 00:00:00","")
#implementar hora do inicio e hora do fim
    hora = str(tabela_data['H'][i])

    path = Service(r"C:\Users\pc\Documents\PIBIC_PY\geckodriver.exe")
    navegador = webdriver.Firefox(service=path)
    navegador.get('https://www.avl.class.noaa.gov/saa/products/search?sub_id=0&datatype_family=GRGLMPROD&submit.x=25&submit.y=3')
    time.sleep(5)

    navegador.find_element_by_xpath('//*[@id="start_date"]').clear()
    navegador.find_element_by_xpath('//*[@id="start_date"]').send_keys(data) # (format: YYYY-MM-DD)

    navegador.find_element_by_xpath('//*[@id="end_date"]').clear()
    navegador.find_element_by_xpath('//*[@id="end_date"]').send_keys(data) # (format: YYYY-MM-DD)

    navegador.find_element_by_xpath('//*[@id="start_time"]').clear()
    navegador.find_element_by_xpath('//*[@id="start_time"]').send_keys(hora) # (format: HH:MM:SS)

    navegador.find_element_by_xpath('//*[@id="end_time"]').clear()
    navegador.find_element_by_xpath('//*[@id="end_time"]').send_keys(hora) # (format: HH:MM:SS)

    navegador.find_element_by_xpath('//*[@id="advanced"]/table/tbody/tr/td[1]/input').click()

    navegador.find_element_by_id('G16').click()

    navegador.find_element_by_xpath('//*[@id="searchbutton"]').click()

    time.sleep(4)
    navegador.find_element_by_xpath('//*[@id="contentArea"]/page/div[2]/form[2]/table[2]/tbody/tr[2]/td[2]/input').click()
# Testando para ver se tem 2 dados para o mesmo tempo.
    try:
        navegador.find_element_by_xpath('//*[@id="contentArea"]/page/div[2]/form[2]/table[2]/tbody/tr[3]/td[2]/input').click()
    except NoSuchElementException:
        print("O elemento " + str(i) + " da tabela nao tem 2 tempos.")
    print("##########################################################")
    #####-------------#####
    navegador.find_element_by_xpath('//*[@id="contentArea"]/page/div[2]/form[2]/table[1]/tbody/tr/td[2]/input[1]').click()
    time.sleep(4)
# Faz o login
    navegador.find_element_by_xpath('//*[@id="midNavElements"]/li[2]/a').click()
    time.sleep(2)
    navegador.find_element_by_name('j_username').send_keys(nome)
    navegador.find_element_by_name('j_password').send_keys(senha)
    navegador.find_element_by_xpath('//*[@id="contentArea"]/div/form/input[3]').click()

# Finaliza pedido
    # navegador.find_element_by_xpath('//*[@id="contentArea"]/form[2]/div[2]/input[1]').click()
    time.sleep(5)
    navegador.close()

print("#### Finalizando o BOT ####")