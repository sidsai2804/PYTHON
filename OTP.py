import smtplib
import random

def generate_otp():
    return str(random.randint(100000, 999999))

otp = generate_otp()

email = "unknowngamer28o4@gmail.com"
password = "leagntwoebwjwcnz"
recever_mail = "sidsai28@gmail.com"

message = f'''FROM: {email}
TO: {recever_mail}
CC: {recever_mail}
SUBJECT: Another mail \n
This is your one-time password {otp}'''

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()
server.login(email, password)
server.sendmail(email, recever_mail, message)
print("Email sent")
server.quit()

user_entered_otp = input("Enter the OTP received in your email: ")

if user_entered_otp == otp:
    print("OTP verification successful! Access granted.")
else:
    print("Incorrect OTP. Access denied.")
