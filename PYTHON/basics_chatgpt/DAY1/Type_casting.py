#converting one datatype to another is called type casting
age = int(input("Enter age: "))
print("Age is :", age)

"""
🧠 Types
int()
float()
str()
bool()
"""
#🔥 TRICKY QUESTION 5
print(int("10") + int("20"))
print("10" + "20")
# in the first line we are converting the strings "10" and "20" to integers and then adding them, which gives us 30
# in the second line we are concatenating the strings "10" and "20", which gives us "1020"