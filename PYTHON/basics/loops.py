#while loops:execute some code WHILE a condition is true
# i = 1
# while i <= 5:
#     print(i)
#     i += 1  # increment i by 1
# print("While loop ended")

# name=input("enter the name:")
# while name=="":
#     print("you did not enter a name")
#     name=input("enter the name:") #chance to enter name again 
# print("hello "+name)

# #AGE CALCULATION:
# age=int(input("enter the age:"))
# while age<0:
#     print("you have entered the wrong age")
#     age=int(input("enter the age again:"))
# print(f"Hello, your age is: {age}")

# #FOOD CALCULATION:
# food=input("enter the food you want to order:")
# while food=="":
#     print("you did not enter any food")
#     food=input("enter the food you want to order:")
# print("your order for "+food+" has been placed")

# num=int(input("enter a number:"))
# while num<1 or num>10:
#     print("number is out of range")
#     num=int(input("enter a number again:"))
# print("you have entered a valid number:",num)

"""---------------------FOR LOOPS------------------"""

# #for loops:iterate over a sequence (like a list, tuple, string) or other iterable objects
 
# for x in range(1,6):
#     print(x)
# print("for loop ended")
""" All numbers in the the same line"""
# for i in range(1,11):
#     print(i, end=" ")
    #prints numbers from 1 to 10 in the same line



# #reverse a string using for loop
# for x in reversed(range(1,11)):
#     print(x)
# print("Happy New Year!")

# #count 1 to 10 having step 2
# for x in range(1,11,2):
#     print(x)

# #credit card number 
# credit_number="1234-5678-9101-1121"
# for digit in credit_number:
#      print(digit)


# ##continue statement in for loop:
# for i in range(1,21):
#     if i==13:
#         continue
#     print(i)
# #skips 13 and prints from 1 to 20

# ##break statement in for loop:
# for i in range(1,21):
#     if i==13:
#         break
#     print(i)

#     #prints 1 to 12 and breaks the loop at 13

##jump statement in for loop:
# for i in range(1,21):
#     if i%2==0:
#         pass
#     else:
#         print(i)  ##prints all odd numbers from 1 to 20

"""---------------------NESTED LOOPS------------------"""
# #nested loops: a loop inside another loop
"""1)while loop inside another while loop
   2)for loop inside another for loop
   3)while loop inside for loop
    4)for loop inside while loop
"""
#example for ,FOR loop inside another FOR loop
for i in range(3):
    for j in range(1,5):
        print(j,end=" ")
    print()  #new line after inner loop ends
    #prints 1 to 4 three times

# """ create the matrix   for having the 012 012 012"""
# rows=int(input("enter number of rows:")) #3
# cols=int(input("enter number of columns:")) #3
# for i in range(rows):
#     for j in range(cols):
#         print(j,end=" ")
#     print()  #new line after inner loop ends

rows=int(input("enter number of rows:")) 
cols=int(input("enter number of columns:"))
symbol=input("enter the symbol to print:")
for x in range(rows):
    for y in range(cols):
        print(symbol,end=" ")
    print()  #new line after inner loop ends


"""example of while loop inside another while loop"""

