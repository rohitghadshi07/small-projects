import re

email_condition = '^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

def email_validator(email):
    
    if (re.search(email_condition,email)):
        print('Valid Email')
    else:
        print('Invalid Email')


email = input("Enter EmailAddress:")

email_validator(email)
