from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import logging

logging.getLogger('selenium').setLevel(logging.DEBUG)

# Seadistame Chrome WebDriver
driver = webdriver.Chrome()  

# Ava Google'i avaleht
driver.get('https://www.google.com')

# Leia otsingukast (sisend element)
search_box = driver.find_element(By.NAME, 'q')

# Sisestage otsingupäring
search_query = 'Automating Google Search with Selenium'
search_box.send_keys(search_query)

# Esitage otsinguvorm (klõpsake Enter)
search_box.send_keys(Keys.RETURN)

# Oodake, et tulemused laaditakse (valikuline, kuid võib olla kasulik)
driver.implicitly_wait(5)  # Ootame kuni 5 sekundit, et tulemused laaditaks

# Läbige otsingutulemusi ja klõpsake tulemusi (valikuline)

# Sulgege brauser
driver.quit()


# Leia esimene otsingutulemus ja klõpsa sellel
first_result = driver.find_element(By.CSS_SELECTOR, 'h3')
first_result.click()



