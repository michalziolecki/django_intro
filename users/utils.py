import base64
import hashlib
import os


def hash_password_without_salt(password: str) -> str:
    # hashing password
    return hashlib.sha3_512(password.encode('ascii')).hexdigest()  # utf-8 ascii can be used for encoding


def verify_password_without_salt(password: str, stored_password: str) -> bool:
    pwd_hash = hashlib.sha3_512(password.encode('ascii')).hexdigest()
    return stored_password == pwd_hash


def hash_with_salt_password(password: str) -> str:
    # creating salt
    random_size = 30
    salt: str = hashlib.sha3_512(os.urandom(random_size)).hexdigest()
    encoded_salt: bytes = base64.b64encode(salt.encode('ascii'))
    base64_salt: str = str(encoded_salt, 'ascii')

    # hashing password
    pwd = ''.join([password, base64_salt])
    pwd_hash = hashlib.sha3_512(pwd.encode('ascii')).hexdigest()
    hex_pwd = ''.join([pwd_hash, base64_salt])
    base64_pwd: bytes = base64.b64encode(hex_pwd.encode('ascii'))
    final_pwd_hash: str = str(base64_pwd, 'ascii')
    password = ''.join([final_pwd_hash, base64_salt])
    return password


def verify_password_with_salt(password: str, stored_password: str) -> bool:
    salt_len = 172
    base64_salt: str = stored_password[-salt_len:]
    pwd = ''.join([password, base64_salt])
    pwd_hash = hashlib.sha3_512(pwd.encode('ascii')).hexdigest()
    hex_pwd = ''.join([pwd_hash, base64_salt])
    base64_pwd: bytes = base64.b64encode(hex_pwd.encode('ascii'))
    final_pwd_hash: str = str(base64_pwd, 'ascii')
    return ''.join([final_pwd_hash, base64_salt]) == stored_password

