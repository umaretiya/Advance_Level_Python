import re
# a-z
# 0-9
# . _ 1 time
# @ 1 time
# . from last 2,3

email_conditioon = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input("Enter your Email")

if re.search(email_conditioon, user_email):
    print("Right email")
else:
    print("wrong email")



