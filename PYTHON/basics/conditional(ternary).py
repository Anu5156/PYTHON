#conditonal (ternary) operator:
#A shoerthand of if-else statement that evaluates a condition and returns one of two values based on whether the condition is true or false.
 
## even or odd
# NUM=int(input("Enter a number: "))
# #print "Even" if NUM is even else print "Odd"
# result = "Even" if NUM % 2 == 0 else "Odd"
# print(result)

# a=6
# b=7
# max_value = a if a > b else b
# min_value = a if a < b else b
# print("The maximum value is:", max_value)
# print("The minimum value is:", min_value)
# # Output: The maximum value is: 7
# # Output: The minimum value is: 6

#to check adult or not
age = int(input("Enter your age: "))
voter_status = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(voter_status)
# Output will depend on the input age

#to check positive, negative or zero
num = int(input("Enter a number: "))
result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(result)