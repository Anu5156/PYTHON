#if else if statementsblock another if else if statenent is called nested if
num = 10

if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("And it is even.")
    else:
        print("And it is odd.")
else:
    print("The number is non-positive.")


age=29
income=35000
if age>=26 :
    print("your age is suffient")
    if income>=30000 :
        print("You are eligible to get marriage")
    else:
        print("you are not eligible to get marriage")
else:
    print("your age is not sufficient")


x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
else:
   print("print higher value")

age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")



score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")


username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")


score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")