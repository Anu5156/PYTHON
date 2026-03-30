#logical operators:evaluate multiple conditions(and,or,not)

 # or: at least one condition is true
age = 17
has_id = True

if age >= 18 or has_id:
    print("Allowed to enter")
else:
    print("Not allowed")
               


#and: all conditions must be true
not_raining = True
is_daytime = True
if not_raining and is_daytime:
    print("Go out and Play!")
else:
    print("Stay indoors.")



#not: negates the condition
is_raining = False

if not is_raining:
    print("You can go outside")
else:
    print("Take an umbrella")
