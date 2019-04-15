import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://kyoumu.is.it-chiba.ac.jp/campusweb3.5/top.do')
time.sleep(0.5)

driver.find_element_by_id("userId").send_keys("")
driver.find_element_by_id("password").send_keys("")
time.sleep(1)
driver.find_element_by_id("loginButton").click()



from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, features="html.parser")

print(soup.title.string)