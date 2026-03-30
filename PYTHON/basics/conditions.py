#if :Do something code only IF some condition is True Else do something else
 #VOTING ELIGIBILITY(example)
age=int(input("enter your age:"))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


#HAVE A FOOD OR NOT(example)
food=input("do you have food? (yes/no):")
if food=="yes":
    print("You can eat the food")
else:
    print("You need to buy food")

# FOR A SALE:
amount=int(input("enter the bill amount:"))
if amount>1000:
    discount=amount*0.1
    final_amount=amount-discount
    print("You got a discount of:",discount)
    print("Final amount to be paid:",final_amount)
else:
    print("No discount applicable")
    print("Final amount to be paid:",amount)


#if-elif-else: Do something code if some condition is True Else if another condition is True Do something else Else do something else(example)
#GRADE CALCULATION
marks=int(input("enter your marks:"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=40:
    print("Grade D")
else:
    print("Grade F")


#Another example traffic light
color=input("enter the traffic light color:")
if color=="red":
    print("Stop")
elif color=="yellow":
    print("Wait")
elif color=="green":
    print("Go")
else:
    print("Invalid traffic light color")


#NESTED IF-ELSE: if-else inside another if-else(example)
age=int(input("enter your age:"))
if age>=18:
    if age>=65:
        print("You are eligible to vote and also a senior citizen")
    else:
        print("You are eligible to vote but not a senior citizen")
else:
    print("You are not eligible to vote")