"""
@author:86152
@file:用户类.py
@time:2021/11/03
"""
class User():
    __userID = None
    __username =None
    __password = None
    __address = None
    __money = None
    __registerDate = None
    __bank_name = "中国工商银行"
    def setUserID(self,userID):
        self.__userID = userID
    def getUserID(self):
        return self.__userID
    def setUsername(self,username):
        self.__username = username
    def getUsername(self):
        return self.__username
    def setPassword(self,password):
        self.__password = password
    def getPassword(self):
        return self.__password
    def setAddress(self,address):
        self.__address = address
    def getAddress(self):
        return self.__address
    def setMoney(self,money):
        self.__money = money
    def getMoney(self):
        return self.__money
    def setRegistertime(self,registertime):
        self.__registertime=registertime
    def getRegistertime(self):
        return self.__registertime
    def setBank_name(self,bank_name):
        self.__bank_name = bank_name
    def getBank_name(self):
        return self.__bank_name

