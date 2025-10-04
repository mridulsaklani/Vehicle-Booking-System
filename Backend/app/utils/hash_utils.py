import hashlib
from passlib.hash import bcrypt

def hash_email(email:str )-> str:
    return hashlib.sha256(email.encode()).hexdigest()

def hash_pass(password: str)->str:
    return bcrypt.hash(password)

def validate_pass(password: str, hashed_password: str)-> bool:
    return bcrypt.verify(password, hashed_password)