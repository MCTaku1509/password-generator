import random
import string
import secrets

string_length = 20

#Password recommendation with a combination of uppercase letters lower case letters, and punctuation
pwd = ''.join(secrets.choice(string.ascii_letters + string.punctuation)for x in range(string_length))

#Password recommendation with a combination of uppercase and lowercase letters, special characters and numbers
pwd1 = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation)for x in range(string_length))

print(pwd)
print(pwd1)
