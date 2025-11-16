
import random

import string 


password_len = int(input("Enter your password length"))

def generate_password(password_len):
    password = ""
    letters = string.ascii_letters
    digits = string.digits
    speacial = string.punctuation

    all_characters = letters + digits + speacial 

    for i in range(password_len):
        password += random.choice(all_characters)
    return password

my_password = generate_password(password_len)

print("Your password is ",my_password)

