import re

email_pattern = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
check_email = email_pattern.fullmatch('saurabh_1089@gmail.com')

# at least 8 characters long
# contains any sort of letter, numbers, $%#@
# has to end with a number
password_patter = re.compile(r"([a-zA-Z0-9@#$%]{8,}\d)")
check_password = password_patter.fullmatch('edtrswe#$%9')

if check_email and check_password:
    print("Both email and password are correct.")
else:
    print("Try again.")

'''
password is also checking for minimum 8 chars
'''