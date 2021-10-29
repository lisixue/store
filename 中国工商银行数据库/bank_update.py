"""
@author:86152
@file:day_6_bank.py
@time:2021/10/18
"""
print("*"*30)
print("*          中国工商银行        *")
print("*          账户管理系统        *")
print("*             V1.0           *")
print("*"*30)
print("*           1、开户           *")
print("*           2、存钱           *")
print("*           3、取钱           *")
print("*           4、转账           *")
print("*           5、查询           *")
print("*           6、Bye！          *")
import random
from dbbank import *
bank_name="中国工商银行"  #为全局变量

#调用的函数元素是一一对应的，不是名称对应
def bank_add(account):
    sql_count = "select count(*) from user"
    param = []
    count = select(sql_count,param)
    if count[0][0] >= 100:          #用户库超过100个用户
        return 3

    sql_account = "select account from user"
    param = []
    count = select(sql_account,param)
    for i in count:
        if account in i:            #用户是否已经存在，存在返回2，用户已存在
            return 2
    return 1                 #正常添加用户

def Useradd():

    account=random.randint(10000000,99999999)  #随机生成一个8位数的账号
    username=input("请输入您的姓名：")
    while True:
        password=input("请输入您的密码：")
        if password.isdigit() and len(password)==6:
            break
        else:print("密码格式不对，请重新输入")
    print("下面请输入您的地址：")
    country=input("\t\t请输入您的国家：")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    money=0
    add = bank_add(account)
    if add ==3:
        print("数据库已满，请到其他银行开户")
    elif add ==2:
        print("用户已存在")
    elif add ==1:
        sql_insert = "insert into user value(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
        param = [account,username,password,country,province,street,door,money,bank_name]
        update(sql_insert, param)

        print("开户成功，以下为您的账户信息：")
        info = '''
            --------个人信息--------
            姓名：%s
            账户：%s
            密码：%s
            国家：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s

        '''
        print(info %(username,account,len(password)*"*",country,province,street,door,money,bank_name))
def put_money():                           #存钱
    while True:
        account =int(input("请输入账号："))
        change_money = int(input("请输入金额："))
        sql_account = "select * from user where account = %s"
        param = [account]
        data = select(sql_account, param)
        if len(data) != 0:
            if change_money >0:
                sql_putmoney = "update user set money = money + %s where account = %s"
                param = [change_money,account]
                update(sql_putmoney, param)
                sql_money = "select * from user where account = %s"
                param = [account]
                data = select(sql_money,param)
                print("该账号的的余额为：",data[0][7])
                return 0
            elif change_money <= 0:
                print("金额输入错误")
        else:
            print("该账号不存在")

def account_password(account,password):    #判断账号密码是否正确
    sql_account = "select * from user where account = %s"
    param = [account]
    data_account = select(sql_account,param)
    for i in data_account:
        if account in i:
            sql_password = "select * from user where account = %s"
            param = [account]
            data =select(sql_password,param)
            if password == data[0][2]:
                return 0     #正常
            else:
                print("密码不正确")
                return 2     #密码不对
        else:
            print("该用户不存在")
            return 1         #账号不对
def get_money():     #取钱
    account = int(input("请输入账号："))
    password = int(input("请输入密码："))
    money = int(input("请输入要取出的金额："))
    sql_account = "select * from user where account = %s"
    param = [account]
    data = select(sql_account, param)
    if account_password(account, password) ==0:
        if data[0][7] >= money:
            sql_getmoney = "update user set money = money - %s where account = %s"
            param = [money,account]
            update(sql_getmoney,param)
            print("取钱成功")
            sql_select = "select * from user where account = %s"
            param = [account]
            data = select(sql_select,param)
            print("该账号现在的余额为：",data[0][7])
            return 0
        else:
            print("取钱失败，您的钱不够")
            return 3    #钱不够
    elif account_password(account, password) ==1:
        print("该用户不存在")
        return 1
    else:
        print("密码不对")
        return 2

def transfer():
    account1 = int(input("请输入账号："))
    password1 = int(input("请输入密码："))
    # account2 = int(input("请输入您要转账的账号："))
    # money = int(input("请输入要取出的金额："))
    sql_account = "select * from user"
    param = []
    data_account = select(sql_account, param)
    if account_password(account1,password1) ==0:
        account2 = int(input("请输入您要转账的账号："))
        for i in data_account:
            if account2 in i:
                money = int(input("请输入您要转出的金额："))
                if data_account[0][7] >= money:
                    sql_transfer = "update user set money = money - %s where account = %s"
                    param = [money, account1]
                    update(sql_transfer, param)
                    print("转账成功")
                    sql_select = "select * from user where account = %s"
                    param = [account1]
                    data = select(sql_select, param)
                    print("该账号现在的余额为：", data[0][7])
                    return 0
                else:
                    print("您的钱不够，转账失败")
                    return 3
            else:
                print("转入的账号不对")
                return 1
    elif account_password(account1,password1) ==1:
        print("转出的账号不对")
        return 1
    elif account_password(account1,password1) ==2:
        print("转出的密码不正确")
        return 2

def find():
    account = int(input("请输入账号："))
    sql_account = "select * from user"
    param = []
    data_account = select(sql_account,param)
    for i in data_account:
        if account in i:
            password = int(input("请输入密码："))
            sql_password = "select * from user where account = %s"
            param = [account]
            data_password = select(sql_password,param)
            if password == data_password[0][2]:
                print("当前账号为:",account,"密码为:",password,f"用户居住地址为:",
                      data_account[0][3],data_account[0][4],data_account[0][5],data_account[0][6],
                      "当前账户的开户行为:",data_account[0][9])
                break
            else:
                print("密码输入错误")
                return 0
        else:
            print("该用户不存在")
            return 1

while True:
    index=int(input("请输入您要办理的业务："))
    if index ==1:
        Useradd()
    elif index ==2:
        put_money()
    elif index ==3:
        get_money()
    elif index ==4:
        transfer()
    elif index ==5:
        find()
    elif index ==6:
        print("退出成功")
        break
    else:
        print("没有该业务，请重新输")


