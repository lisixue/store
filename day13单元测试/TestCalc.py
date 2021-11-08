"""
@author:86152
@file:单元测试.py
@time:2021/11/08
"""
'''
    unittest:单元测试框架
    
    1.子类继承TestCase
    2.写测试用例：testXXXX
    任务1：
        使用邮件发送测试报告
        温馨提示：用户名，密码（smtp授权码开通）
    任务2：
        执行减法、乘法、除法测试用例，并生成测试报告
    
'''
from 计算器 import Calc
from unittest import TestCase
class TestCalcAdd(TestCase):
    def testAdd1(self):
        a = 6
        b = 5
        s = 11

        calc = Calc()
        sum = calc.add(a,b)
        self.assertEqual(s,sum)

    def testAdd2(self):
        a = -6
        b = -5
        s = -11

        calc = Calc()
        sum = calc.add(a,b)
        self.assertEqual(s,sum)

    def testAdd3(self):
        a = -6
        b = 5
        s = -1

        calc = Calc()
        sum = calc.add(a,b)
        self.assertEqual(s,sum)

class TestCalcMinus(TestCase):
    def testMinus1(self):
        a = 6
        b = 3
        m = 3

        calc = Calc()
        minus = calc.minus(a,b)
        self.assertEqual(m,minus)

    def testMinus2(self):
        a = 3
        b = 6
        m = -3

        calc = Calc()
        minus = calc.minus(a,b)
        self.assertEqual(m,minus)


class TestCalcMulti(TestCase):
    def testMulti1(self):
        a = 3
        b = 6
        n = 18

        calc = Calc()
        multi = calc.multi(a,b)
        self.assertEqual(n,multi)

    def testMulti2(self):
        a = 4
        b = 3
        n = 12

        calc = Calc()
        multi = calc.multi(a,b)
        self.assertEqual(n,multi)

class TestCalcDevision(TestCase):
    def testDevision1(self):
        a = 6
        b = 3
        p = 2

        calc = Calc()
        devision = calc.devision(a,b)
        self.assertEqual(p,devision)

    def testDevision2(self):
        a = 8
        b = 4
        p = 2

        calc = Calc()
        devision = calc.devision(a,b)
        self.assertEqual(p,devision)






