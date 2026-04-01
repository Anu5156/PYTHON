#precedence operator:
#It defines the order in which operators are evaluated in an expression
"""common precedence order(high--->low)
1.Parenthesis,**
2.Unary operators(++,--,!)
3.Multiplication,division,modulus(*,/,%)
4.Addition,Subtraction(+,-)
5.Comparison(<,>,==)
6.Logical operators(&&,||)
7.Assignment(=,+=,etc)
"""
#ex:
b=6/2+3**4
print(b)#84
#how it works:
#3**4=81
#6/2=3
#-->3+81=84

#ex2:
c=25/(3+2)**2
print(c)
#first preference is parentesis so solve that first:3+2=5
#next is '^' --->**    5**2-->5^2-->25
#25/25=1
#final answer:1


#when 2 or more operators has same precedence python follows associativity
"""LEFT TO RIGHT YOU HAVE TO GO!!!"""
#IF BOTH ARE ** ** THEN IT FOLLOWS Right to leftalso lowest precedence like
"""=,+=,-=,*=,/=are lowest precedence and follows the Right to left"""

#ex:having same precedence with same operator
2**3**2
#<-------
#3**2=3^2=9
2**9=2^9=512
#final answer:512

#ex2:having same precedence with different operator:
y=5*2//3
#output:10//3-->floor division:3.33333===>3

