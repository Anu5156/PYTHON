#python  simple calculator
#functions: add, subtract, multiply, divide
operator=input("Enter the operator (+, -, *, /): ")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
if operator=='+':
    print("Result:", num1+num2)
elif operator=='-':
    print("Result:", num1-num2)
elif operator=='*':
    print("Result:", num1*num2)
elif operator=='/':
    print("Result:", num1/num2)
else:
    print("Invalid operator,enter the valid operator")
