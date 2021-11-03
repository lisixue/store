"""
@author:86152
@file:业务界面.py
@time:2021/11/03
"""
welcome = '''
******************************
*          中国工商银行        *
*          账户管理系统        *
*             V1.0           *
******************************
*           1、开户           *
*           2、存钱           *
*           3、取钱           *
*           4、转账           *
*           5、查询           *
*           6、Bye！          *

'''
class Welcome:
    def serve(self):
        print(welcome)


w=Welcome()
w.serve()

