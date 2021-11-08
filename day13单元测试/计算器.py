"""
@author:86152
@file:计算器.py
@time:2021/11/08
"""

class Calc:

    def add(self,a,b):
        return a+b

    def minus(self,a,b):
        return a-b

    def multi(self,a,b):
        return a*b

    def devision(self,a,b):
        return a/b

# 准备数据
a = 6
b = 3
c = 9
d = 3
e = 18
f = 2

# 执行测试
calc = Calc()

s = calc.add(a,b)
m = calc.minus(a,b)
multi = calc.multi(a,b)
devision = calc.devision(a,b)

# 对比实际结果与期望结果是否一样，看用例是否通过
# if s != c:
#     print("用例不通过")
# else:
#     print("用例通过")
#
# if m != d:
#     print("用例不通过")
# else:
#     print("用例通过")
#
# if multi != e:
#     print("用例不通过")
# else:
#     print("用例通过")
#
# if devision != f:
#     print("用例不通过")
# else:
#     print("用例通过")





