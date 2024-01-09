import smtplib
import random

def generate_otp():
    return str(random.randint(100000, 999999))

otp = generate_otp()
print(f"Generated OTP: {otp}")


#smtp --> simple Mail Transfer Protocol


email = "***********@gmail.com"
password = "*************"
recever_mail = "*********@gmail.com"

message = f'''FROM : {email}
TO: {recever_mail}
CC: {recever_mail}
SUBJECT :  Another mail \n
This is your one time password {otp}'''
# POP, IMAP , SMTP
server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()
server.login(email, password)
server.sendmail(email, recever_mail, message)
print("Email sent")
server.quit()
