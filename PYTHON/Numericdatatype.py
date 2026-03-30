#NUMERIC TYPE:int,float,complex
d = 42
print(type(d))#output: <class 'int'>, because the variable d is of type integer (int) in Python.

e = 3.14
print(type(e))#output: <class 'float'>, because the variable e is of type float in Python.

f = 2 + 3j
print(type(f))#output: <class 'complex'>, because the variable f is of type complex in Python, which represents a complex number with a real part (2) and an imaginary part (3j). j is used to denote the imaginary part in Python is root(-1).


b= -5
print(type(b))#output: <class 'int'>, because the variable b is of type integer (int) in Python, even though it is a negative number.

d= -3.24563
print(type(d))#output: <class 'float'>, because the variable d is of type float in Python, even though it is a negative number.

v= 2**300
print(type(v))#output: <class 'int'>, because in Python, integers can grow arbitrarily large as needed, so even though 2**300 is a very large number, it is still of type int.

b=2**-3
print(type(b))#output: <class 'float'>, because 2**-3 is equivalent to 1/(2**3) which is 1/8 or 0.125, and in Python, this results in a float type.

#how to print real part and imaginary part separately in complex number
print(f.real) #output: 2.0, because the real part of the complex number f (which is 2 + 3j) is 2.0.
print(f.imag) #output: 3.0, because the imaginary part of the complex number f (which is 2 + 3j) is 3.0.

