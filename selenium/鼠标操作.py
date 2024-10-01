from time import sleep
# 导入selenium包
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# 启动并打开指定页面
browser = webdriver.Chrome()
browser.get("https://www.csdn.net")
browser.maximize_window()
sleep(2)
# 创建ActionChains对象
action = ActionChains(browser)
# 定位标签并将鼠标移入,并呈现移入结果
tag = browser.find_element(By.XPATH, '//div/a[@class="btn-write-new"]')
action.move_to_element(tag).perform()
sleep(3)
tag = browser.find_element(By.CSS_SELECTOR, '.blog-nav-box')
action.move_to_element(tag).perform()
sleep(2)
browser.find_element(By.LINK_TEXT, "数学").click()
# 关闭浏览器
sleep(2)
browser.quit()
