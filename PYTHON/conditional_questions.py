#Implement check loan eligibility code that determines persons loan eligibiliy on below condition
"""1.the person should be at least 18 years old
   2.if the income is greater than 30,000 or more
       credit score 700+ :prime loan
       credit score 600-699:standard loan
       credit score below 600:high 
    3.if income less than 20,000:not eligible"""

income=35000
age=20
credit_score=750
if income>30000:
    if credit_score >=700 :
        print("prime loan")
    elif (600<credit_score and credit_score<699):
        print("Standard loan")
    else:
        print("High rise")
elif income<20000:
    print("Not eligible")
else:
    print("take loan safely on your risk")

#output:prime loan

#write a program to check if an year is leap year or not
"""A year is a leap year if it is divisible by 4
   However,if year is also divisible by 100,it is not leap,
   The year is also divisible by 400.Then it is a leap year
"""
year =int(input("enter the year:"))
if(year %4 ==0):
    if(year%100==0):
        if(year%400 == 0):
            print("Its a leap year")
        else:
            print("Nota leap year")
    else:
        print("Its a leap year")
else:
    print("Its not a leap")
"""enter the year:2026
Its not a leap

enter the year:2027
Its not a leap
                  """

#Even or Odd
num=int(input("Enter the number"))
if((num//2)*2==num):
    print("The number is even")
else:
    print("the number is odd")

#Positive,Negative,Zero
num5=int(input("enter the number:"))
if num5<0:
    print("the number is negative")
elif num5>0:
    print("The number is Positive")
else:
    print("The number is Zero")


#triangle validator
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle ")

    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle ")

#grade system
#days in month
#tax calculator
#credit card validator


card = input("Enter card number: ")

# remove spaces
card = card.replace(" ", "")

total = 0
reverse_card = card[::-1]

for i in range(len(reverse_card)):
    n = int(reverse_card[i])

    if i % 2 == 1:   # double every second digit
        n = n * 2
        if n > 9:
            n = n - 9

    total = total + n

# check validity
if total % 10 == 0:
    print("Valid Credit Card ")
else:
    print("Invalid Credit Card ")
