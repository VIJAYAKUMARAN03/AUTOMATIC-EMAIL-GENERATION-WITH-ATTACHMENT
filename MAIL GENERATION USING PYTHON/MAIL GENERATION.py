# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 18:12:22 2022

@author: DELL
"""

import os
from email.message import EmailMessage
import ssl
import smtplib
from emails import names
from images import image
from sub_body import SUB, BODY
sender='vijayakumaran27062003@gmail.com'#sender mail
password='pass'#sender password
receiver=names()
sub=SUB()
body=BODY()
context=ssl.create_default_context()
for i in receiver:
    em=EmailMessage()
    em['From']=sender
    em['Subject']=sub
    body1=body.replace('NAME',i[1])
    em.set_content(body1)
    em['To']=i[0]
    r=image(i[1])
    with open('draw.jpg','rb') as f:
        data=f.read()
        em.add_attachment(data,maintype='application',subtype='jpg',filename=i[1]+' CERTIFICATE.jpg')
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as mail:
        mail.login(sender,password)
        mail.sendmail(sender,i[0],em.as_string())
    os.remove('draw.jpg')
    print(i[1],'- MAIL SENT')

