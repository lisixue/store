"""
@author:86152
@file:bank.py
@time:2021/11/04
"""
import random
import pymysql

# 定义数据库工具类
class DBUtils():
    # 全局增删改的方法
    def update(self,sql,param):
        con = pymysql.connect(host="localhost",user="root",password="root",database="bank")
        cursor = con.cursor()
        cursor.execute(sql,param)
        con.commit()
        cursor.close()
        con.close()

    # 全局做查询的方法
    def select(self,sql,param):
        con = pymysql.connect(host="localhost",user="root",password="root",database="bank")
        cursor = con.cursor()
        cursor.execute(sql,param)
        con.commit()
        data = cursor.fetchall()
        cursor.close()
        con.close()
        return data

class ICBC():
    # 银行的名称写死
    def __init__(self):
        self.bank_name = "中国工商银行的昌平支行"
        self.db = DBUtils()

    # 1.入口程序
    @staticmethod
    def welcome():
        print("*************************************")
        print("*        中国工商银行昌平支行           *")
        print("*************************************")
        print("*              1.开户                *")
        print("*              2.存钱                *")
        print("*              3.取钱                *")
        print("*              4.转账                *")
        print("*              5.查询                *")
        print("*              6.Bye！               *")
        print("**************************************")

    # 2.开户
    # 2.1银行的开户逻辑
    def bank_addUser(self, username):
        # 1.判断数据库是否已满
        sql_count = "select count(*) from user"
        param = []
        count = self.db.select(sql_count, param)
        if count[0][0] >= 100:
            return 3

        # 2.判断用户是否存在
        sql_username = "select username from user"
        param = []
        select_username = self.db.select(sql_username, param)
        for i in select_username:
            if username in i:
                return 2
        return 1

    # 2.2用户的开户的操作逻辑
    def addUser(self):
        account = random.randint(10000000, 99999999)  # 随机生成一个8位数的账号
        username = input("请输入您的姓名：")
        while True:
            password = input("请输入您的密码：")
            if password.isdigit() and len(password) == 6:
                break
            else:
                print("密码格式不对，请重新输入")
        print("下面请输入您的地址：")
        country = input("\t\t请输入您的国家：")
        province = input("\t\t请输入您的省份")
        street = input("\t\t请输入您的街道")
        door = input("\t\t请输入您的门牌号")
        money = 0
        add = self.bank_addUser(account)
        if add == 3:
            print("数据库已满，请到其他银行开户")
        elif add == 2:
            print("用户已存在")
        elif add == 1:
            sql_insert = "insert into user value(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
            param = [account, username, password, country, province, street, door, money, self.bank_name]
            self.db.update(sql_insert, param)

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
            print(info % (username, account, len(password) * "*", country, province, street, door, money, self.bank_name))

    # 3.存钱
    def putMoney(self):
        while True:
            account = int(input("请输入账号："))
            change_money = int(input("请输入金额："))
            sql_account = "select * from user where account = %s"
            param = [account]
            data = self.db.select(sql_account, param)
            if len(data) != 0:
                if change_money > 0:
                    sql_putmoney = "update user set money = money + %s where account = %s"
                    param = [change_money, account]
                    self.db.update(sql_putmoney, param)
                    sql_money = "select * from user where account = %s"
                    param = [account]
                    data = self.db.select(sql_money, param)
                    print("该账号的的余额为：", data[0][7])
                    return 0
                elif change_money <= 0:
                    print("金额输入错误")
            else:
                print("该账号不存在")


    # 判断账户密码是否正确
    def account_password(self,account,password):
        sql_account = "select * from user where account = %s"
        param = [account]
        data_account = self.db.select(sql_account,param)
        for i in data_account:
            if account in i:
                sql_password = "select * from user where account = %s"
                param = [account]
                data = self.db.select(sql_password,param)
                if password == data[0][2]:
                    return 0
                else:
                    print("密码不正确")
                    return 2
            else:
                print("该用户不存在")
                return 1

    # 4.取钱
    def getMoney(self):
        account = int(input("请输入账号："))
        password = int(input("请输入密码："))
        money = int(input("请输入要取出的金额："))
        sql_account = "select * from user where account = %s"
        param = [account]
        data = self.db.select(sql_account, param)
        if self.account_password(account, password) == 0:
            if data[0][7] >= money:
                sql_getmoney = "update user set money = money - %s where account = %s"
                param = [money, account]
                self.db.update(sql_getmoney, param)
                print("取钱成功")
                sql_select = "select * from user where account = %s"
                param = [account]
                data = self.db.select(sql_select, param)
                print("该账号现在的余额为：", data[0][7])
                return 0
            else:
                print("取钱失败，您的钱不够")
                return 3  # 钱不够
        elif self.account_password(account, password) == 1:
            print("该用户不存在")
            return 1
        else:
            print("密码不对")
            return 2

    # 5.转账
    def transferMoney(self):
        account1 = int(input("请输入账号："))
        password1 = int(input("请输入密码："))
        # account2 = int(input("请输入您要转账的账号："))
        # money = int(input("请输入要取出的金额："))
        sql_account = "select * from user"
        param = []
        data_account = self.db.select(sql_account, param)
        if self.account_password(account1, password1) == 0:
            account2 = int(input("请输入您要转账的账号："))
            for i in data_account:
                if account2 in i:
                    money = int(input("请输入您要转出的金额："))
                    if data_account[0][7] >= money:
                        sql_transfer = "update user set money = money - %s where account = %s"
                        param = [money, account1]
                        self.db.update(sql_transfer, param)
                        print("转账成功")
                        sql_select = "select * from user where account = %s"
                        param = [account1]
                        data = self.db.select(sql_select, param)
                        print("该账号现在的余额为：", data[0][7])
                        return 0
                    else:
                        print("您的钱不够，转账失败")
                        return 3
                else:
                    print("转入的账号不对")
                    return 1
        elif self.account_password(account1, password1) == 1:
            print("转出的账号不对")
            return 1
        elif self.account_password(account1, password1) == 2:
            print("转出的密码不正确")
            return 2

    # 6.查询
    def find(self):
        account = int(input("请输入账号："))
        sql_account = "select * from user"
        param = []
        data_account = self.db.select(sql_account, param)
        for i in data_account:
            if account in i:
                password = int(input("请输入密码："))
                sql_password = "select * from user where account = %s"
                param = [account]
                data_password = self.db.select(sql_password, param)
                if password == data_password[0][2]:
                    print("当前账号为:", account, "密码为:", password, f"用户居住地址为:",
                          data_account[0][3], data_account[0][4], data_account[0][5], data_account[0][6],
                          "当前账户的开户行为:", data_account[0][9])
                    break
                else:
                    print("密码输入错误")
                    return 0
            else:
                print("该用户不存在")
                return 1

class ICBCMain():
    def __init__(self):
        self.icbc = ICBC()

    def run(self):
        # 添加死循环，让程序入口重复显示
        while True:
            self.icbc.welcome()
            # 获取用户的输入选择,根据用户的输入选择进行判断
            chose = input("请输入您的业务：")
            if chose == "1":
                self.icbc.addUser()
            elif chose == "2":
                self.icbc.putMoney()
            elif chose == "3":
                self.icbc.getMoney()
            elif chose == "4":
                self.icbc.transferMoney()
            elif chose == "5":
                self.icbc.find()
            elif chose == "6":
                print("Bye! 欢迎下次光临！")
                break
            else:
                print("输入错误！请重新输入！")

# 程序启动
m = ICBCMain()
m.run()


