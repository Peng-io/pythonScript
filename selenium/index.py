from selenium import webdriver
from selenium.webdriver.common.by import By
# Chrome浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
driver.get('https://www.baidu.com/')
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.ID,"kw").send_keys("csdn")
driver.find_element(By.ID,"su").click()
