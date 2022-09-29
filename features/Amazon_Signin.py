from selenium import webdriver
from selenium.webdriver.common.by import By

c = webdriver.ChromeOptions()
c.add_argument("--incognito")

driver = webdriver.Chrome(executable_path='C:\\Users\\suman\\OneDrive\\Desktop\\python-selenium-automation\\chromedriver.exe', options=c)
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()

expected_result = 'Sign in'

actual_result = driver.find_element(By.XPATH, "//h1[@class= 'a-spacing-small']").text

assert expected_result == actual_result, f'Error: Expected {expected_result}, but got {actual_result}'
assert driver.find_element(By.ID, 'ap_email'), 'Email field not shown'
driver.quit()


