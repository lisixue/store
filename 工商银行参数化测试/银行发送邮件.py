"""
@author:86152
@file:银行发送邮件.py
@time:2021/11/10
"""

import zmail

# 读取计算器.html的内容 --》文件操作
# 打开文件

msg_content = {
    'subject' : '这是李思雪的工商银行测试报告',
    'headers' : '测试报告',
    'attachments' :r'C:\Users\86152\Desktop\day14【参数化测试】\bank.xls'
}

reviceser = "842904325@qq.com"

sender={'username':'842904325@qq.com','pwd':'chiolmdvdbvhbbci'}

server=zmail.server(sender['username'],sender['pwd'])
server.send_mail(reviceser,msg_content)





