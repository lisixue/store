"""
@author:86152
@file:发送邮件2.py
@time:2021/11/08
"""
'''
导包：import zmail
读取计算器.html文件内容：with open(filename,mode) as f 或者 file = open(filename,mode)
添加邮件内容，包含：主题（subject）、正文（content_text)、附件（attchments）  ——一般存在字典里
添加发件人，包含：发件人账号，密码（授权码）——一般存在字典中
添加收件人，包括收件人地址，如果有多个收件人则用列表存储
发送邮件
发件人登录：server=zmail.server(username,password)
发件人发送邮件，出入收件人地址，邮件内容 server.send_email(revicer,email_content)

'''
import zmail

# 读取计算器.html的内容 --》文件操作
# 打开文件
file = open(r'C:\Users\86152\PycharmProjects\pythonProject\day_13单元测试\计算器.html','r',encoding ='utf-8')
msg = file.read()
msg_content = {
    'subject' : '这是李思雪的计算器的测试报告',
    'content_html' : msg,
    'attachments' :['计算器.html']
}

reviceser = "2431320433@qq.com"

sender={'username':'842904325@qq.com','pwd':'chiolmdvdbvhbbci'}

server=zmail.server(sender['username'],sender['pwd'])
server.send_mail(reviceser,msg_content)






