from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'https://portal.cfm.org.br/busca-medicos/'

options = Options()
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)
driver.maximize_window()

for timer in range(20):
    sleep(1)
    print(timer+1)

element = driver.find_element(By.ID, 'uf')
element.send_keys('pr')
element.send_keys(Keys.ENTER)
sleep(1)
element = driver.find_element(By.ID, 'municipio')
element.send_keys('cascavel')
sleep(1)
element.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="buscaForm"]/div/div[4]/div[2]/button').click()

for i in range(3):

    if i > 0:
        if (i + 1 >= 6) and (i < 200):
            xpath = '//*[@id="paginacao"]/div/div/ul/li[6]/a'
        if i == 199:
            xpath = '//*[@id="paginacao"]/div/div/ul/li[7}]/a'
        else:
            xpath = f'//*[@id="paginacao"]/div/div/ul/li[{i + 1}]/a'
        driver.find_element(By.XPATH, xpath).click()

    sleep(6)
    element = driver.find_element(By.CLASS_NAME, 'busca-resultado')
    txt_file = open("data.txt", "a")
    txt_file.write(element.get_attribute('innerHTML'))
    txt_file.close()



