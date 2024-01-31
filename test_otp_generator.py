import pytest
from OtpGenerator import OTPGenerator

@pytest.fixture
def otp_generator():
    sender_email = 'sharmagautam2811@gmail.com'
    sender_password = 'purjnoylbryghwaz'
    twilio_account_sid = 'ACbe42830956f02da22e321dff91ab99f1'
    twilio_auth_token = '3f879200374cc6bfcca3e0617f86593e'
    twilio_number = '+17272314733'

    return OTPGenerator(sender_email, sender_password, twilio_account_sid, twilio_auth_token, twilio_number)

def test_validate_email_valid():
    otp_generator_instance = otp_generator()
    result = otp_generator_instance.validate_email("sharmagautam2811@gmail.com")
    expected = True
    assert result == expected

def test_validate_email_invalid():
    otp_generator_instance = otp_generator()
    result = otp_generator_instance.validate_email("sharmagautamgmaicom")
    expected = False
    assert result == expected

def test_generate_otp():
    otp_generator_instance = otp_generator()
    generated_otp = otp_generator_instance.generate_otp()
    otp_str = str(generated_otp)
    otp_len = len(otp_str)
    expected_len = 6
    assert otp_len == expected_len

    otp_type = otp_str.isdigit()
    expected_type = True
    assert otp_type == expected_type
