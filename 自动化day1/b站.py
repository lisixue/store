"""
@author:86152
@file:b站.py
@time:2021/11/15
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r'https://www.bilibili.com')

driver.maximize_window()

driver.find_element('xpath',"//*[@autocomplete='off']").send_keys("易烊千玺舞蹈")

time.sleep(2)
driver.find_element('xpath',"//*[@class='nav-search-btn nav-search-btn-exper nav-search-btn-exper3 nav-search-btn-exper4 nav-search-btn-exper4-hover']").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element('xpath',"/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li[2]/a").click()

time.sleep(2)
driver.find_element('xpath',"//*[@class='like on']").click()


driver.quit()



