"""
@author:86152
@file:main.py
@time:2021/11/08
"""

'''
    1.加载所有的测试用例
    2.执行用例并生成测试报告

'''
from HTMLTestRunner import HTMLTestRunner
import unittest

# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"C:\Users\86152\PycharmProjects\pythonProject\day_13单元测试",pattern="Test*.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "计算器的测试报告",
    description= "这是测试报告",
    verbosity= 1,
    stream = open(file = "计算器.html",mode= "w+",encoding="utf-8")
)

# 3.执行用例
runner.run(tests)






