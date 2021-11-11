"""
@author:86152
@file:IP统计.py
@time:2021/11/11
"""

f = open(file = "baidu_x_system.log",mode= "r+",encoding="utf-8")

data = f.readlines()  #将所有行的路径，存在列表中

list = []
count = {}
for i in data:
    ip =  i.split(" ",1)
    list.append(ip[0])

for i in list:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
print(count)


