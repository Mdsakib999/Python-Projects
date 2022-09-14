#Password generator Program...

import string
import random

character = list(string.ascii_letters + string.digits + "!@#$%&*()")

def password_genarator():

    pass_length = int(input("How many characters of password you want: "))
    random.shuffle(character)

    password = []

    for i in range(pass_length):
        password.append(random.choice(character))

    random.shuffle(password)

    password = "".join(password)

    print(password)


Option = input("Do you want to generate a password? Yes/No :")

if Option == "Yes" or Option =="yes":
    password_genarator()

elif Option == "No" or Option == "no":
    print("The --End--")

else:
    print("Invalid input, Enter Yes or No")