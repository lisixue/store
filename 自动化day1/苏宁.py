"""
@author:86152
@file:苏宁.py
@time:2021/11/15
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()


driver.get(r'https://www.suning.com')

driver.maximize_window()

driver.find_element('xpath',"//*[@id='searchKeywords']").send_keys("冰箱")

driver.find_element('xpath',"//*[@id='searchSubmit']").click()

time.sleep(2)
driver.find_element('xpath',"/html/body/div[10]/div/ul/li[7]/div/div/div[1]/div/a/img").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.find_element('xpath',"//*[@id='addCart']").click()






