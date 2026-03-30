#validate user input exercise
# 1. username is no more then 12 characters
# 2.username must not contain any spaces
#3.username must not contain digits
import string
username=input("enter the user name:")
if len(username)>12:
    print("username must be no more then 12 characters")
elif  not username.find(" ")==-1:
    print("Username contains spaces")
elif not username.isalpha():
    print("username must not contain the digits and the specialcharacters ")
else:
    print(f"welcome {username}")
