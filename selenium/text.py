from time import sleep
# 导入selenium包
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# 启动并打开指定页面
browser = webdriver.Chrome()
browser.get("https://www.csdn.net")
sleep(2)
input_text = browser.find_element(By.XPATH, '//*[@id="toolbar-search-input"]')
input_text.send_keys("selenium")
sleep(2)
input_text.send_keys(Keys.CONTROL, "a")  # 全选
sleep(2)
input_text.send_keys(Keys.CONTROL, 'x')  # 剪切
sleep(2)
input_text.send_keys(Keys.CONTROL, 'v')  # 粘贴
sleep(2)
input_text.send_keys(Keys.BACK_SPACE)  # 回退一格
# 关闭浏览器
sleep(2)
browser.quit()
