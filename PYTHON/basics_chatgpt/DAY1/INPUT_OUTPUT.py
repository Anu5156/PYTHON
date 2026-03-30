#taking input
name = input("Enter your name: ")
print("My name is:", name)

# only input always comes for string

#for example if we want to take age
age = input("Enter age: ")
print(type(age))#string becoz we have used only input
# if we want to take age as integer then we have to type cast it
age = int(input("Enter age: "))
print(type(age))#integer becoz we have type casted it to int


#🔥 TRICKY QUESTION 4
age = input("Enter age: ")
print(age + 5)# this will give error because age is string and we are trying to add integer to it

# to fix this, we need to type cast the input to integer
age = int(input("Enter age: "))
print(age + 5)# this will now work correctly,by adding 5 to the current age which you have entered.
