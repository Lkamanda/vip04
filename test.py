import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import traceback

my_sender = "18612463553@163.com"
my_passwd = "5211314zxy."
my_user = "m13231533164@163.com"
my_smtp_host = 'smtp.163.com'  # 126的smtp服务器地址


def mail():
    ret = True
    try:
        # 开始打包邮件
        msg = MIMEMultipart()
        msg['From'] = my_sender
        msg['To'] = my_user
        msg['Subject'] = '这个是邮件的主题'
        # 下面是正文内容
        file = r'C:\Users\zhoujialin\PycharmProjects\interface\testReport\xiaolin.html'
        pureText = MIMEText(open(file, 'rb').read(), 'html', 'utf-8')
        # 随便找的html文件，后面两个参数是告诉程序以html格式和utf-8字符
        print(pureText)
        msg.attach(pureText)

        # 下面是各种类型的附件了
        # # 首先是xlsx类型的附件
        # xlsxpart = MIMEApplication(open(r'C:\Users\zhoujialin\PycharmProjects\interface\testReport\xiaolin.html', 'rb').read())
        # xlsxpart.add_header('Content-Disposition', 'p_w_upload', filename='test.xlsx')
        # msg.attach(xlsxpart)

        # jpg类型的附件/html
        jpgpart = MIMEApplication(open(r'C:\Users\zhoujialin\PycharmProjects\interface\testReport\xiaolin.html', 'rb').read())
        jpgpart.add_header('Content-Disposition', 'p_w_upload', filename='xiaolin1.html')
        msg.attach(jpgpart)
        # 下面开始发送了
        server = smtplib.SMTP(my_smtp_host)  # smtp服务器端口默认是25
        # server.set_debuglevel(1)# 设置为调试模式，就是在会话过程中会有输出信息
        server.login(my_sender, my_passwd)
        server.sendmail(my_sender, my_user, msg.as_string())
        server.quit()
    except Exception as e:
        print(e)
        ret = False
    return ret


ret = mail()
if ret:
    print("ok")
else:
    print('failed')