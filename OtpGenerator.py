#Importing Libraries
from twilio.rest import Client
import random
import smtplib

# Constants
SENDERS_EMAIL = 'sharmagautam2811@gmail.com'
SENDERS_PASSWORD = 'purjnoylbryghwaz'
TWILIO_ACCOUNT_SID = 'ACbe42830956f02da22e321dff91ab99f1'
TWILIO_AUTH_TOKEN = '3f879200374cc6bfcca3e0617f86593e'
TWILIO_NUMBER = '+17272314733'

#Generating otp
def generate_otp():
    return random.randint(100000, 999999)

#Validating email
def validate_email(email):
    return '@' in email and '.' in email

#Validating mobile number
def validate_mobile(mobile):
    return len(mobile) == 10 and mobile.isdigit()

#Sending otp over email
def send_otp_over_email(receiver_email, otp):
    message = 'Your OTP is ' + str(otp)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SENDERS_EMAIL, SENDERS_PASSWORD)
    server.sendmail(SENDERS_EMAIL, receiver_email, message)
    server.quit()
    print("OTP sent successfully to", receiver_email)

#Sending otp over sms
def send_otp_over_mobile(target, otp):
    if validate_mobile(target):
        target = "+91" + str(target)
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body="Your OTP is " + str(otp),
            from_=TWILIO_NUMBER,
            to=target
        )
        print("OTP Sent to {} successfully".format(target))
    else:
        print("Enter a valid mobile number!")

#Main
def main():
    print("\n*******************<< OTP Generator >>*******************")
    otp = generate_otp()

    # Sending OTP over Email
    print("\nSending OTP via Email")
    receiver_email = input("Enter your Email: ")
    if validate_email(receiver_email):
        send_otp_over_email(receiver_email, otp)
    else:
        print("Please enter a valid email!")

    # Sending OTP over SMS
    print("\nSending OTP via SMS")
    target_mobile = input("Enter Mobile number: ")
    send_otp_over_mobile(target_mobile, otp)

if __name__ == "__main__":
    main()
