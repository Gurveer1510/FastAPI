from passlib.hash import bcrypt

def hash(passkey):
    hashed_password = bcrypt.using(rounds=13).hash(passkey)

    return hashed_password
