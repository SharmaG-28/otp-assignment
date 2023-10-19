from OtpGenerator_Version_3 import generate_otp, validate_email, validate_mobile

def test_generate_otp():
    otp = generate_otp()
    assert 100000 <= otp <= 999999

def test_validate_email():
    assert validate_email("test@example.com") is True
    assert validate_email("invalid_email") is False

def test_validate_mobile():
    assert validate_mobile("1234567890") is True
    assert validate_mobile("12345") is False
