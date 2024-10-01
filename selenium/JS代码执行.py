from time import sleep
# 导入selenium包
from selenium import webdriver
# 启动并打开指定页面
browser = webdriver.Chrome()
browser.get("https://www.csdn.net")
browser.maximize_window()
sleep(2)
# 执行js弹窗代码
browser.execute_script("alert('这是js弹窗代码')")
sleep(2)
browser.switch_to.alert.accept()
sleep(2)
# 执行js窗口滚动条代码
browser.execute_script("window.scrollTo(20,1000)")
sleep(2)
# 打开多个窗口
browser.execute_script("window.open('https://www.baidu.com')")
browser.execute_script("window.open('https://www.bing.com')")
sleep(2)
browser.quit()
