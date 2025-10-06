
import smtplib
from email.message import EmailMessage
from app.constants.enums import OTP_TYPE

import os



EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_otp_email(to_email: str, otp: str, subject: str):
    mail_subject = ""
    match subject:
        case OTP_TYPE.VERIFICATION:
            mail_subject = "Otp for email verification"
            return
        case OTP_TYPE.RESET_PASSWORD:
            mail_subject = "Otp for reset password"
            return
        case OTP_TYPE.LOGIN:
            mail_subject = "Otp for login request"
            return
        case _:
            mail_subject = "mujhe bhi nahi pata"

    print("to email: ", to_email, "otp: ", otp)
    msg = EmailMessage()
    msg["Subject"] = mail_subject
    msg["From"] = EMAIL_USER
    msg["To"] = to_email
    msg.set_content(f"Your OTP is: {otp}\n\n Expire with 10 min \n\n Please do not share it with anyone.")

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_USER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return {"message": "OTP email sent successfully", "status": True }
    except Exception as e:
        print(f"err aa gya bc: {e} ")
        return {"error": str(e)}


