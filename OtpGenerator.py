import smtplib
import random

otp = random.randint(100000, 999999)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sharmagautam2811@gmail.com','purjnoylbryghwaz')

message = 'Your otp is '+str(otp)
reciever_mail = input("Enter your mail : ")

server.sendmail('sharmagautam2811@gmail.com',reciever_mail , message)
server.quit()
print("OTP sent sucessfully")
