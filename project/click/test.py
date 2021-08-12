from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
#today
search = driver.find_element_by_name('s')
search.send_keys('test')
search.send_keys(Keys.RETURN)
#today
driver.get("https://techwithtim.net")
print(driver.title)