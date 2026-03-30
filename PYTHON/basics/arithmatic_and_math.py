#SHORTHAND ARITHMETIC OPERATORS
#count
# count=10
# #count=count+1
# count+=1 #add 1 to count
# count-=2 #subtract 2 from count
# count*=3 # multiply count by 3
# count/=2 # divide count by 2
# count//=2 #floor divide count by 2
# count**=2 #raise count to the power 2
# count%=3 #modulus count by 3
# print(f"The final value of count is: {count}")

x=3.14
y=7.94
# rounding off
result=x+y
print(f"The sum is:{result} and the rounded of the sum is:{round(result)}")

#absolute value
num=-10
print(f"The absolute value of {num} is:{abs(num)}")

#power
x=5
print(f"{x} raised to the power {2} is:{pow(x,2)}")

#square root
import math
num_sqrt=16
print(f"The square root of {num_sqrt} is:{math.sqrt(num_sqrt)}")

#maximum and minimum
a=10
b=20
print(f"The maximum between {a} and {b} is:{max(a,b)}")
print(f"The minimum between {a} and {b} is:{min(a,b)}")

#logarithm
num_log=100
print(f"The logarithm base 10 of {num_log} is:{math.log10(num_log)}")
print(f"The natural logarithm of {num_log} is:{math.log(num_log)}")

#factorial
num_fact=5
print(f"The factorial of {num_fact} is:{math.factorial(num_fact)}")
#trigonometric functions
angle_deg=30
angle_rad=math.radians(angle_deg)
print(f"The sine of {angle_deg} degrees is:{math.sin(angle_rad)}")
print(f"The cosine of {angle_deg} degrees is:{math.cos(angle_rad)}")
print(f"The tangent of {angle_deg} degrees is:{math.tan(angle_rad)}")
print(f"The arcsine of 0.5 is:{math.degrees(math.asin(0.5))} degrees")
print(f"The arccosine of 0.5 is:{math.degrees(math.acos(0.5))} degrees")
print(f"The arctangent of 1 is:{math.degrees(math.atan(1))} degrees")

#degrees to radians and vice versa
print(f"{angle_deg} degrees is:{angle_rad} radians")
print(f"{angle_rad} radians is:{math.degrees(angle_rad)} degrees")

#random number generation
import random
random_num=random.randint(1,100)
print(f"A random number between 1 and 100 is:{random_num}")
random_float=random.uniform(1.0,10.0)
print(f"A random float between 1.0 and 10.0 is:{random_float}")
random_choice=random.choice(['apple','banana','cherry','date'])
print(f"A random choice from the list is:{random_choice}")

#combinations and permutations
from math import comb, perm
n=5
r=3
print(f"The number of combinations of {n} choose {r} is:{comb(n,r)}")
print(f"The number of permutations of {n} choose {r} is:{perm(n,r)}")
