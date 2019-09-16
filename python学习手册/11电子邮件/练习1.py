'''
特别注意:目前大多数邮件服务商都需要手动打开SMTP发信和POP收信的功能，否则只允许在网页登录

一封电子邮件的旅程就是：
发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

要编写程序来发送和接收邮件，本质上就是：
1.编写MUA把邮件发到MTA；
3.编写MUA从MDA上收邮件。

发邮件时，MUA和MTA使用的协议就是SMTP,后面的MTA到另一个MTA也是用SMTP协议。
收邮件时，MUA和MDA使用的协议有两种：POP：Post Office Protocol，目前版本是3，俗称POP3；
IMAP：目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。

Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，
传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
'''
import smtplib
from email.mime.text import MIMEText

from_addr='zheng606524@163.com'
password='zhang606524'
to_addr='2297113361@qq.com'
smtp_server='smtp.163.com'          #SMTP服务器地址

#写一封完整邮件(收件人，发件人，主题，正文)
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')       #邮件正文
#标准邮件需要三个头部信息： From, To, 和 Subject(主题)
message['From'],message['To'],message['Subject'] = from_addr,to_addr,'Python SMTP 邮件测试'

s=smtplib.SMTP(smtp_server,25)      #SMTP协议的默认端口是25
#s.set_debuglevel(1)                #打印出和SMTP服务器交互的所有信息,SMTP协议就是简单的文本命令和响应
s.login(from_addr,password)         #登录SMTP服务器
try:
    print('开始发送邮件...')
    #发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
    s.sendmail(from_addr,[to_addr],message.as_string())
    print('邮件发送成功!')
except Exception as e:
    print('Error:无法发送邮件',e)
s.quit()
