a=int(input("enter the first_number:"))
b=int(input("enter the second_number:"))
operator=input("Enter the operator:")
if operator=="+":
    print("the sum of ",a,"and",b,"is",a+b)
elif operator=="-":
    print("the difference of ",a,"and",b,"is",a-b)
elif operator=="*":
    print("the product of ",a,"and",b,"is",a*b)
elif operator=="/":
    print("the quotient of ",a,"and",b,"is",a/b)
else:
    print("Invalid operator")