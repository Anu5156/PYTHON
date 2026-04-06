#if-else-if 
#else is the shorter form of else-if,it is used to check for multiple condition
#if condition of if is false,it checks for subsequent elif block till condition is true.
#If all the condition are false,then else is executed

"""syntax:
if(expression):
    statement 1
    statemnet 2
elif(expression):
    statement 1
    statemnet 2
elif(expression):
    statement 1
    statemnet 2
else:
     statement 1
    statemnet 2

"""
"""WAP  to take char input from the user and check if its (A)capital letter
(b)small letter,(c)digit (d)special symbol"""

char=(input("enter the character:"))
if(char>='a' and char<='z'):
    print("Its a small letter")
elif(char>='A' and char<='Z'):
    print("Its a capital")
elif(char>='0' and char <='9'):
    print("Its a number")
else:
    print("Its a special symbol")
"""output: enter the character:A
           Its a capital
           enter the character:8
           Its a number"""

marks=int(input("Enter the marks:"))
if(marks>=90):
    print("O")
elif(80<=marks<90):
    print("A")
elif(70<=marks<80):
    print("B")
elif(60<=marks<70):
    print("C")
else:
    print("You are fail")
"""Enter the marks:76
   B"""



