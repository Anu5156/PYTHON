#PATTERN 1

for i in range(1, 5):#i takes values from 1 to 4
    print("*" * i)
#output:  * 
        # **
        # *** 
        # ****
#PATTERN 2
"""
1
12
123
1234
"""
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()#for new line after each row

#PATTERN 3
"""
****
***
**
*
"""
for i in range(4,0,-1):
    print("*" * i)
    # print("")

#PATTERN 4
"""
1
22
333
4444
"""
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end="")
    print()#for new line after each row

"""PATTERN 5
1
01
101
0101
"""
for i in range(1,5):
    for j in range(1,i+1):
        print((i+j-1)%2,end="")
    print()#for new line after each row
"""
🔥 MAIN LOGIC
(i + j - 1) % 2

👉 This creates alternating pattern

🧠 WHY THIS WORKS

👉 Let’s simplify:

(i + j) decides parity (even/odd)

Even → 0
Odd → 1
🔍 TRACE (VERY IMPORTANT)
👉 Row 1 (i = 1)
j	(i+j-1)	%2	Output
1	1+1-1 = 1	1	1

👉 Output: 1

👉 Row 2 (i = 2)
j	(i+j-1)	%2	Output
1	2+1-1 = 2	0	0
2	2+2-1 = 3	1	1

👉 Output: 01

👉 Row 3 (i = 3)
j	(i+j-1)	%2	Output
1	3	1	1
2	4	0	0
3	5	1	1

👉 Output: 101

👉 Row 4 (i = 4)
j	(i+j-1)	%2	Output
1	4	0	
2	5	1	
3	6	0	
4	7	1	

👉 Output: 0101

🧠 SIMPLE RULE (REMEMBER THIS)

(i + j) % 2 → alternating pattern
Adjust with -1 to control starting value"""