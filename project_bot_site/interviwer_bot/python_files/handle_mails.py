import smtplib


def send_email_otp():
    global otp
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(host_email_addr, host_email_pass)
        # calling method for generating otp
        otp = generate_otp()
        subject = 'From Travel India :: OTP for verifying your E-mail.'
        body = '\n\n\nThe otp for login is '+otp+'. Don`t share with anyone.'
        msg = f'Subject: {subject}\n\n\n{body}'

        smtp.sendmail(host_email_addr, email_signup, msg)
        print("E-mail sent successfully..!")


def generate_otp():
    otp = ""
    for i in range(6):
        otp = str(otp + random.choice(otp_list))
        print("otp : ", otp)
    print("final otp is : ", otp)
    print("otp generated successfully..!")
    return otp



