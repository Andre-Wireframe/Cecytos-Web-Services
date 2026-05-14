from pymongo import MongoClient
import bcrypt

def encript(password):
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt)

def check_password(password, hash):
    password_bytes = password.encode("utf-8")
    hash_bytes = hash.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hash_bytes)

