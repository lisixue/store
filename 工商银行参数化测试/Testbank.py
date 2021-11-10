"""
@author:86152
@file:Testbank.py
@time:2021/11/09
"""
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from 工商银行完整版 import bank_addUser
from 工商银行完整版 import bank_saveMoney
from 工商银行完整版 import bank_takeMoney
import xlrd
from xlutils.copy import copy

# username,password,country,province,street,door,money
rb =xlrd.open_workbook(r"C:\Users\86152\Desktop\day14【参数化测试】\bank.xls",encoding_override=True)
r_sheet = rb.sheet_by_index(0)
rows = r_sheet.nrows
da = []

for i in range(1,rows):
    value = r_sheet.row_values(i)
    value.pop()
    da.append(value)



sheet2 = rb.sheet_by_index(1)
rows = sheet2.nrows
da2 = []
for j in range(1,rows):
    value2 = sheet2.row_values(j)
    value2.pop()
    da2.append(value2)


sheet3 = rb.sheet_by_index(2)
rows = sheet3.nrows
da3 = []
for j in range(1,rows):
    value3 = sheet3.row_values(j)
    value3.pop()
    da3.append(value3)

wb = copy(rb)
w_sheet = wb.get_sheet(0)
w_sheet2 = wb.get_sheet(1)
w_sheet3 = wb.get_sheet(2)

@ddt
class TestBank(TestCase):
    @data(*da)
    @unpack
    def testAddUser(self,username,password,country,province,street,door,money,excepted_result,s):
        result = bank_addUser(username,password,country,province,street,door,money)

        if result == excepted_result:
            w_sheet.write(s,9,'通过')
            wb.save(r"C:\Users\86152\Desktop\day14【参数化测试】\bank.xls")
        else:
            w_sheet.write(s,9,'不通过')
            wb.save(r"C:\Users\86152\Desktop\day14【参数化测试】\bank.xls")

        self.assertEqual(excepted_result,result)

    @data(*da2)
    @unpack
    def testsavemoney(self,account,money,excepted_result,s):    #存钱
        result = bank_saveMoney(account,money)

        if result == excepted_result:
            w_sheet2.write(s,4,'通过')
            wb.save(r"C:\Users\86152\Desktop\day14【参数化测试】\bank.xls")
        else:
            w_sheet2.write(s,4, '不通过')
            wb.save(r"C:\Users\86152\Desktop\day14【参数化测试】\bank.xls")

        self.assertEqual(excepted_result,result)

    @data(*da3)
    @unpack
    def testtakemoney(self,account,password,money,excepted_result,s):   #取钱
        result = bank_takeMoney(account,password,money)

        if result == excepted_result:
            w_sheet3.write(s,5,'通过')
            wb.save(r"C:\Users\86152\Desktop\day14【参数化测试】\bank.xls")
        else:
            w_sheet3.write(s, 5, '不通过')
            wb.save(r"C:\Users\86152\Desktop\day14【参数化测试】\bank.xls")






