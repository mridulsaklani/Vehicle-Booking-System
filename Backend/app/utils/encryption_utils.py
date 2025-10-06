import os

from cryptography.fernet import Fernet

fernet_secret_key = os.getenv("FERNET_SECRET_KEY")
# print("key",Fernet.generate_key().decode())
# print("secret key: ", fernet_secret_key)

if not fernet_secret_key:
    raise ValueError("FERNET_SECRET_KEY not found in environment variables.")

fernet = Fernet(fernet_secret_key)

def incrept_email(email: str)-> str:
    encrypt_mail = fernet.encrypt(email.encode()).decode()
    
    return encrypt_mail  

def decrept_email(encryptEmail: str)->str:
    email = fernet.decrypt(encryptEmail.encode()).decode()
    
    return email

def incrept_data(data: str)-> str:
    return fernet.encrypt(data.encode().decode())

def decrept_data(data: str)-> str:
    return fernet.decrypt(data.encode().decode)