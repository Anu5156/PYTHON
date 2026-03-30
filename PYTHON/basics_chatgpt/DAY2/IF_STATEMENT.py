#if condition: Runs only if condition is true
age=int(input("enter the age:"))
if age>18:
    print("you are eligible to vote")
#here if we enter the age less than 18 then it will not print anything because the condition is false

#always indentation matters:..INDENTATION?:the space of 4 or the one time pressing the tab.is called indentation
x = 10
if x > 5:
    print("Greater")

#💣 TRICKY QUESTION 1
x = 10

if x > 5:
    print("A")
if x > 8:
    print("B")
#output:A B
#HERE BOTH THE CONDITIONS ARE TRUE SO BOTH THE PRINT STATEMENT WILL BE EXECUTED