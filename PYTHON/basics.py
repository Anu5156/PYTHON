print("hello")
#output: hello

print(1+2)
#output: 3

print("1"+"2")
#output: 12,because the + operator concatenates the two strings together instead of performing addition.

#using f-string to print the value of a variable
a="Anushka"
print(f"hello {a}")
#output: hello Anushka, because the f-string allows us to embed the value of the variable a directly into the string.

#normal way to print the value of a variable
print("hello",a)
#output: hello Anushka, because the print function can take multiple arguments and will separate them with a space by default.

print("hello"+"world")
#output: helloworld, because the + operator concatenates the two strings together without adding a space.

print("hello","world")
#output: hello world, because the print function separates the two arguments with a space by default.

#BUILT IN FUNCTIONS
# 1.print() #used to display output to the console.
# 2.input() #used to take input from the user.

#TO TAKE THE INPUT FROM THE USER
name = input("Enter your name: ")
print("your name is :", name)
#output: Enter your name: Anushka
#your name is : Anushka, because the input function prompts the user to enter their name and then stores it in the variable name, which is then printed using the print function.

#to take the input of two numbers and print their sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)
