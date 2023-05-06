import random
import string
import secrets

def pwd_generator(string_length):
    '''Takes password length as an integer and generates a secure
    combination of letters numbers that are suitable for passwords.'''
    pwd = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation)for x in range(string_length))

    return pwd

print(pwd_generator(20))