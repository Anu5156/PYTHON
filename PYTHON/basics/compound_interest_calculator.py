#compound_interest_calculator using while loop
"""
formula: A=P(1+r/n)**t
"""
principal=0
rate=0
time=0

while principal<=0:
    principal=float(input("enter the principal amount:"))
    if principal<=0:
        print("principal amount should be greater than 0")
while rate<=0:
    rate=float(input("enter the rate of interest:"))
    if rate<=0:
        print("rate of interest should be greater than 0")

while time<=0:
    time=int(input("enter the time in years:"))
    if time<=0:
        print("time should be greater than 0")

print(f"principal amount is {principal}")
print(f"rate of interest is {rate}")
print(f"time in years is {time}")

amount=principal*((1+rate/100)**time)
print(f"compound interest is {amount}")