#loops can be nested in python as in other llanguages.
"""Nested loops is a loop that occurs within another loop.
they are  lot helpful in solution pattern questions"""

"""syntax:
for<val> in some_seq:
    s1
    s2
    s3
    for <var2> in some_seq:
        s'1
        s'2
        s'3
s3
<unindented statement>
"""
"""
outer_loop_expression:
    inner_loop_expression:
        I_S1
        I_S2
        I_S3
    O_S1
    O_S2
<unidented code 1>
<unidented code 2>"""

# for i in range(1,11):
#     print("outer loop number",i)
#     for j in range(3,5):
#         print("Inner loop:",i*j)
#     print("outside of inner loop",i)
"""outer loop number 1
Inner loop: 3
Inner loop: 4
outside of inner loop 1
outer loop number 2
Inner loop: 6
Inner loop: 8
outside of inner loop 2
outer loop number 3
Inner loop: 9
Inner loop: 12
outside of inner loop 3
outer loop number 4
Inner loop: 12
Inner loop: 16
outside of inner loop 4
outer loop number 5
Inner loop: 15
Inner loop: 20
outside of inner loop 5
outer loop number 6
Inner loop: 18
Inner loop: 24
outside of inner loop 6
outer loop number 7
Inner loop: 21
Inner loop: 28
outside of inner loop 7
outer loop number 8
Inner loop: 24
Inner loop: 32
outside of inner loop 8
outer loop number 9
Inner loop: 27
Inner loop: 36
outside of inner loop 9
outer loop number 10
Inner loop: 30
Inner loop: 40
outside of inner loop 10"""

#ex1:
# for outer in range(3):       # Outer loop
#     for inner in range(2):   # Inner loop
#         print(outer, inner)
#output:
"""
0 0
0 1
1 0
1 1
2 0
2 1
"""
#print a square pattern
# for i in range(3):
#     for j in range(3):
#         print("*",end=" ")
#     print()
"""
* * *
* * *
* * *
"""

#Print triangle pattern
# for i in range(1, 5):
#     for j in range(i):
#         print("*", end=" ")
#     print()
"""
*
* *
* * *
* * * *
"""

#multiplication table square
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i * j, end=" ")
#     print()
"""
1 2 3
2 4 6
3 6 9
"""
# i = 1
# while i <= 3:
#     j = 1
#     while j <= 3:
#         print(i, j)
#         j += 1
#     i += 1
"""
2 1
2 2
2 3
3 1
3 2
3 3
"""


rows = 5

# for i in range(1, rows + 1):
#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")
    
#     # Print stars
#     for k in range(i):
#         print("*", end=" ")
    
#     print()

"""
         *
        * *
       * * *
      * * * *
     * * * * *
     
     """

"""
1
22
333
4444
55555
"""
# for outer in range(1,6):
#     for inner in range(outer):
#         print(outer,end=" ")
#     print()
