#decision control statement
"""Decision control statement are one those statement which decide the execution flow of the program
In simple words,they tell us whether a particular part of program should run or not to run based upon certain condition"""

"""there are 4 types of conditonal statements"""
#1.if 
#2.if else
#3.if else if
#4.nested if else

#if statemnet:used when certain block of code is executed .if the statement is true then it will executed 
a=20
b=30
if a > b:
    print("A is grater than b")
#output:northing will be executed

c=60
d=12
if c> d:
    print("c is grater than d")
#output:c is grater than d

#python uses indentation:which means 1tab or 4 spaces

number="+91-9908765893"
msg1="You are from India"
msg2="You are not from India"
if ("+91" in number):
    print(msg1)
#output:You are from India

if ("+91" not in number):
    print(msg2)
#output:you are not from India

#wAP to check the number is even
n=int(input("enter the number:"))
if n & 1 ==0:
    print("even")

#checks last binary digits
#even->last bit is 0
#odd->last bit is 1

# if ((n/2)*2)==n:
#     print("even")
# #divide by 2 and multiply is back and check whether the number is equal to input number

# #check whether the number is divisible by both 3 and 5
# n=int(input("enter the number:"))
# if (n%3==0 & n%5==0):
#     print("The number is divisible by both 3 and 5")


