#!/usr/bin/env python
#coding=utf-8
 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
from email import encoders
from datetime import *
import os

def send_mail(server, fro, to, subject, text, files=[]): 
    ''''' 
    server is a dict.
    to is a list.
    files is a list.
    server={"name":"smtp.126.com","user":"xxx@126.com","passwd":"xxx"}
    
    '''
    assert type(server) == dict 
    assert type(to) == list 
    assert type(files) == list 
 
    msg = MIMEMultipart() 
    msg['From'] = fro
    msg['Subject'] = subject 
    msg['To'] = COMMASPACE.join(to)             #COMMASPACE==', ' 
    msg['Date'] = formatdate(localtime=True) 
    msg.attach(MIMEText(text)) 
 
    for attchement in files: 
        part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data 
        part.set_payload(open(attchement, 'rb').read()) 
        encoders.encode_base64(part) 
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attchement)) 
        msg.attach(part) 
 
    import smtplib 
    smtp = smtplib.SMTP(server['name']) 
    smtp.login(server['user'], server['passwd']) 
    smtp.sendmail(fro, to, msg.as_string()) 
    smtp.close()
    
    
if __name__=='__main__':
    server={"name":"smtp.126.com","user":"xxx@126.com","passwd":"xxx"}
    fro="xxx126.com"
    to=["xxx@126.com","xxx@qq.com"]
    subject='email_test %s' % (datetime.now())
    text="This is content."
    #files=[]
    #files=['E:\\gitdir\\learning\\python_learning\\base\\socket\\TCPClient.py']
    files=['TCPClient.py',"TCPServer.py","meitui.jpg"]
    try:
        send_mail(server, fro, to, subject, text, files)
        print "send email ok"
    except Exception as e:
        print "send email error "
        print e