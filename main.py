import time
from selenium import webdriver
import logging
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('C:\\Users\\giuliog\Documents\\webdrivers\\chromedriver.exe')
driver.get('http://apps.tre-sc.jus.br/site/fileadmin/arquivos/eleicoes/estatistica_eleitoral/estat_offline/PerfilEleitor/MunicFE/PerfilMunicFE010820.htm');
try:
    time.sleep(7)

    #toda a tabela
    tableWE = driver.find_element_by_xpath("//table[@class = 'appDataTable']")
    html_content = tableWE.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    tableSOUP = soup.find(name='table')

    df_full = pd.read_html(str(tableSOUP))[0]
    print("\npandas\n")
    print(df_full)
    
    for i in df_full:
        print(i)
    row = df_full.get("Município")    
    print(row)
    idx = 0
    for i in row:
        print("cidade: " + i)
        if i == "DOUTOR PEDRINHO":
            break
        idx += 1
    for key in df_full:
        value = df_full.get(key)[idx]
        print("{}: {}".format(key, value))
    
    time.sleep(5)
except Exception as ex:
    logging.exception("Erro!")
    pass
finally:
    print("quit")
    driver.quit()