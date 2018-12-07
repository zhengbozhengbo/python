import smtplib  # 发送邮件的协议
import email.mime.text  # 处理发送的内容
import email.mime.multipart  #  处理邮件的表头

sender = 'zhengbo19960406@163.com'  #  发送者
recver = ['15837806865@163.com',
          '13346647595.com',
            ]   #  接收者
server = 'smtp.163.com'          #  服务器地址
passwd = 'bo33807358zheng'             #  授权码
# 创建一个空邮件
message = email.mime.multipart.MIMEMultipart()
# 发件人
message['from'] = sender
# 收件人
message['to'] = ','.join(recver)
# 主题
message['subject'] = '555n'
# 正文
text = """
hello wdsasdasdasdasdasda
dasadasdas8 岁!!!!
"""
# 处理文本信息
text = email.mime.text.MIMEText(text)
# 将处理后的信息添加到邮件里
message.attach(text)

# 定义服务器和端口
smtp123 = smtplib.SMTP_SSL(server,465)
# 登录服务器
smtp123.login(sender,passwd)
# 发送邮件
smtp123.sendmail(sender,recver,message.as_string())
# 断开连接
smtp123.close()