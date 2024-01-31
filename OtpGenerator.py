#Importing Libraries
import random
import smtplib
from twilio.rest import Client

# Class OTPGenerator starts here
class OTPGenerator:
    def __init__(self, sender_email, sender_password, twilio_account_sid, twilio_auth_token, twilio_number):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.twilio_account_sid = twilio_account_sid
        self.twilio_auth_token = twilio_auth_token
        self.twilio_number = twilio_number

    # Method for Generating otp
    def generate_otp(self):
        return random.randint(100000, 999999)

    # Method for Validating email
    def validate_email(self, email):
        return '@' in email and '.' in email

    # Method for Validating mobile number
    def validate_mobile(self, mobile):
        return len(mobile) == 10 and mobile.isdigit()

    # Method for Sending otp over email
    def send_otp_over_email(self, receiver_email, otp):
        if self.validate_email(receiver_email):
            message = 'Your OTP is ' + str(otp)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, receiver_email, message)
            server.quit()
            print("OTP sent successfully to", receiver_email)
        else:
            print("Please enter a valid email!")

    # Method for Sending otp over sms
    def send_otp_over_mobile(self, target, otp):
        if self.validate_mobile(target):
            target = "+91" + str(target)
            client = Client(self.twilio_account_sid, self.twilio_auth_token)
            message = client.messages.create(
                body="Your OTP is " + str(otp),
                from_=self.twilio_number,
                to=target
            )
            print("OTP Sent to {} successfully".format(target))
        else:
            print("Enter a valid mobile number!")

    #Main method
    def main(self):
        print("\n*******************<< OTP Generator >>*******************")
        otp = self.generate_otp()

        # Sending OTP over Email
        print("\nSending OTP via Email")
        receiver_email = input("Enter your Email: ")
        self.send_otp_over_email(receiver_email, otp)

        # Sending OTP over SMS
        print("\nSending OTP via SMS")
        target_mobile = input("Enter Mobile number: ")
        self.send_otp_over_mobile(target_mobile, otp)

if __name__ == "__main__":
    sender_email = 'sharmagautam2811@gmail.com'
    sender_password = 'purjnoylbryghwaz'
    twilio_account_sid = 'ACbe42830956f02da22e321dff91ab99f1'
    twilio_auth_token = '3f879200374cc6bfcca3e0617f86593e'
    twilio_number = '+17272314733'

    otp_generator = OTPGenerator(sender_email, sender_password, twilio_account_sid, twilio_auth_token, twilio_number)
    otp_generator.main()
