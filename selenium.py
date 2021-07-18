from selenium import webdriver
from selenium.webdriver.common.by import By

#selenium-python.readthedocs.com to learn more about it
browser = webdriver.Firefox() #it's easier to use firefox
browser.get('https://automatetheboringstuff.com')
elem = browser.find_elements(By.XPATH, "//a[contains(text(),'Creative Common')]")[0].click()
elem.send_keys('your string') # type into 
elem.submit() #submit 
# back(), forward(), refresh()
# quit() => close 