"""🗓️ STEP 5: TRUTHY & FALSY 🔥
🧠 RULE
❌ False(no,negative) values:
0
""
[]
None
✅ Everything else → True"""

if "":
    print("Yes")
else:
    print("No")
#output: No

if " ":
    print("Yes")
else:
    print("No")
#output: Yes

## "" is empty string → Falsy and " " is not empty string → Truthy
bool("")#output:false
bool(" ")#output:true
bool(0)#output:false
bool(1)#output:true
bool([])#output:false
bool([1,2])#output:true

if "0":
    print("True")
else:
    print("False")
#output: True ,because 0 is considered as string and it is not empty string so it is truthy

if 0:
    print("A")
if "0":
    print("B")
#output: only B because 0 is falsy and "0" is truthy

if []:
    print("A")
else:
    print("B")
#output: B because [] is falsy