"""
@author:86152
@file:测试报告.py
@time:2021/11/10
"""
from HTMLTestRunner import HTMLTestRunner
import unittest


tests=unittest.defaultTestLoader.discover(r'C:\Users\86152\PycharmProjects\pythonProject\day_14参数化测试加多线程','Testbank.py')

HTMLTestRunner.HTMLTestRunner(
    title = "中国工商银行测试报告",
    description= "开户、存钱、取钱",
    verbosity=1,
    stream= open(file='Bank.html',mode = 'w+',encoding='utf-8')
).run(tests)







