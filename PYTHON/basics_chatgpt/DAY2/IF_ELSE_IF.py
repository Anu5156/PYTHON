#🧠 IMPORTANT

# 👉 Only FIRST TRUE condition executes

marks = 75
if marks > 90:
    print("A")
elif marks > 70:
    print("B")
else:
    print("C")#prints B

"""🔹 4. Why elif instead of multiple if?"""
# Because elif is more efficient and readable when you want to check multiple conditions in sequence.
"""elif ensures only ONE condition runs
Multiple if will check ALL conditions

x = 10
if x > 5:
    print("A")
if x > 8:
    print("B")
#output: both A B

if x > 5:
    print("A")
elif x > 8:
    print("B")
#output: only A



"""