#concatenation in python
#for string it adds the two strings together
a="Mayank"
b="Anushka"
c=a+b
print(c)
#output: MayankAnushka, because the + operator is used to concatenate the two strings 'Mayank' and 'Anushka', resulting in 'MayankAnushka'.with no space in between. If you want to add a space between the two strings, you can modify the code as follows:

#for number it acts as the arithmatic operator and adds the two numbers together
d=5
e=10
f=d+e
print(f)
#output: 15, because the + operator is used to add the two numbers 5 and 10 together, resulting in 15.

#using arithmatic operator with string and number will give us error

a=15
b="Anushka"
c=a+b
print(c)
#output: TypeError: unsupported operand type(s) for +: 'int' and 'str', because the + operator cannot be used to add an integer (int) and a string (str) together in Python. The types of the operands are incompatible for concatenation or addition, resulting in a TypeError.

#if we add two numbers as string:
a="12"
b="34"
c=a+b
print(c)
#output: 1234, because when we use the + operator with two strings '12' and '34', it concatenates them together, resulting in the string '1234'. The + operator does not perform arithmetic addition in this case, but rather string concatenation.

 #+ operator in string act as the concatenation operator, which combines two strings together without any space, while in the case of numbers, it acts as the addition operator, which sums the values.but if we want the space between the two strings we can add a space in between the two strings as follows:
a="Anushka"
b="pryianka"
c=a+" "+b
print(c)
#output: Anushka pryianka, because the + operator is used to concatenate the two strings 'Anushka' and 'pryianka' with a space in between, resulting in 'Anushka pryianka'.

#print Anushka 10 times
print("Anushka "*10)
#output: Anushka Anushka Anushka Anushka Anushka Anushka Anushka Anushka Anushka Anushka , because the * operator is used to repeat the string 'Anushka ' (with a space at the end) 10 times, resulting in 'Anushka ' repeated 10 times. Note that there is a space after 'Anushka' in the string, so when it is repeated, there will be a space between each occurrence of 'Anushka'.

#only multiplication and addition works with string, other arithmatic operators will give us error

"""multiplication for string is used to repeat the string a certain number of times, while addition is used for concatenation. Other arithmetic operators like subtraction (-), division (/), modulus (%), and exponentiation (**) are not defined for strings and will result in a TypeError if you try to use them with string operands."""

"""SLICING IN PYTHON:pulling of sequence of characters from the string
syntax: string_name[start_index:end_index:step]"""
s="Anushka"
print(s[0:5]) #output: Anush, because the slicing operation s[0:5] extracts the characters from index 0 to index 4 (5 is exclusive) of the string 'Anushka', resulting in 'Anush'.
"stops one step before the end index"

print(s[0:len(s)])
#output:Anushka, because the slicing operation s[0:len(s)] extracts the characters from index 0 to index len(s)-1 (which is the last index of the string) of the string 'Anushka', resulting in the entire string 'Anushka'. The len(s) function returns the length of the string, which is 7 in this case, so the slicing operation effectively retrieves all characters from index 0 to index 6.

#ex2:
s1="Mayank"
print(s1[0:3]) #output: May, because the slicing operation s1[0:3] extracts the characters from index 0 to index 2 (3 is exclusive) of the string 'Mayank', resulting in 'May'.

#ex3:
#POSITIVE INDEXING
s="Python"
print(s[1:4]) #output: yth, because the slicing operation s[1:4] extracts the characters from index 1 to index 3 (4 is exclusive) of the string 'Python', resulting in 'yth'.
print(s[3:10])#output: hon, because the slicing operation s[3:10] extracts the characters from index 3 to index 9 (10 is exclusive) of the string 'Python'. Since the string 'Python' has only 6 characters, the slicing operation effectively retrieves characters from index 3 to index 5.
print(s[0:])
#output:Python
print(s[:])
#output:Python
print(s[2:2])#output:' ', because the slicing operation s[2:2] extracts the characters from index 2 to index 1 (2 is exclusive) of the string 'Python'. Since the start index and end index are the same, it results in an empty string ''.
print(s[4:0])
#output:' ', because the slicing operation s[4:0] extracts the characters from index 4 to index -1 (0 is exclusive) of the string 'Python'. Since the start index is greater than the end index, it results in an empty string ''.

#NEGATIVE INDEXING:
s="Python"
print(s[-1]) #output: n, because the negative index -1 refers to the last character of the string 'Python', which is 'n'.
print(s[-3:-1]) #output: ho, because the slicing operation s[-3:-1] extracts the characters from index -3 to index -2 (since -1 is exclusive) of the string 'Python'. The negative index -3 refers to the third-to-last character, which is 'h', and the negative index -2 refers to the second-to-last character, which is 'o'. Therefore, the result of the slicing operation is 'ho'.
print(s[-4:]) #output: thon, because the slicing operation s[-4:] extracts the characters from index -4 to the end of the string 'Python'. The negative index -4 refers to the fourth-to-last character, which is 't', and since there is no end index specified, it retrieves all characters from index -4 to the end of the string, resulting in 'thon'.
print(s[:-3]) #output: Pyt, because the slicing operation s[:-3] extracts the characters from the beginning of the string 'Python' up to index -4 (since -3 is exclusive). The negative index -3 refers to the third-to-last character, which is 'h'. Therefore, the result of the slicing operation is 'Pyt', which includes the characters from index 0 to index 2 of the string 'Python'.
print(s[-4:-1]) #output: thon, because the slicing operation s[-4:-1] extracts the characters from index -4 to index -2 (since -1 is exclusive) of the string 'Python'. The negative index -4 refers to the fourth-to-last character, which is 't', and the negative index -2 refers to the second-to-last character, which is 'o'. Therefore, the result of the slicing operation is 'thon'.
print(s[-2:-6]) #output:' ', because the slicing operation s[-2:-6] extracts the characters from index -2 to index -5 (since -6 is exclusive) of the string 'Python'. Since the start index (-2) is greater than the end index (-6), it results in an empty string ''.

print(s[:10000000000])#output: Python, because the slicing operation s[:10000000000] extracts the characters from the beginning of the string 'Python' up to index 9999999999 (since 10000000000 is exclusive). Since the string 'Python' has only 6 characters, the slicing operation effectively retrieves all characters from index 0 to index 5, resulting in 'Python'.
print(s[-10000000000:])#output: Python, because the slicing operation s[-10000000000:] extracts the characters from index -10000000000 to the end of the string 'Python'. Since the negative index -10000000000 refers to a position far before the start of the string, it effectively retrieves all characters from the beginning of the string to the end, resulting in 'Python'.
print(s[100:10000])#output:' ', because the slicing operation s[100:10000] extracts the characters from index 100 to index 9999 (since 10000 is exclusive) of the string 'Python'. Since the string 'Python' has only 6 characters, there are no characters at index 100 or beyond, resulting in an empty string ''.

"""INTRODUCING STEP OR STRIDE VALUE IN SLICING:"""
#slicing can accept a 3rd parameter called step or stride . It specifies the step size or the number of characters to skip while slicing the string. The syntax for slicing with a step value is: string_name[start_index:end_index:step].
s="Python"
print(s[0:6:2]) #output: Pto, because the slicing operation s[0:6:2] extracts the characters from index 0 to index 5 (6 is exclusive) of the string 'Python' with a step of 2. This means it retrieves every second character starting from index 0, resulting in 'P', 't', and 'o', which combined gives 'Pto'.
print(s[0:6:3]) #output: Ph, because the slicing operation s[0:6:3] extracts the characters from index 0 to index 5 (6 is exclusive) of the string 'Python' with a step of 3. This means it retrieves every third character starting from index 0, resulting in 'P' and 'h', which combined gives 'Ph'.
#step value is counting the values next to start index and then it is picking the value and then it is counting the values next to the picked value and then it is picking the value and so on until it reaches the end index.
#for example ,if the step size is 2 and the start index is 0, then it will count the values next to index 0 which are index 1 and index 2 and then it will pick the value at index 2 and then it will count the values next to index 2 which are index 3 and index 4 and then it will pick the value at index 4 and so on until it reaches the end index.
print(s[0:6:1]) #output: Python, because the slicing operation s[0:6:1] extracts the characters from index 0 to index 5 (6 is exclusive) of the string 'Python' with a step of 1. This means it retrieves every character starting from index 0, resulting in 'P', 'y', 't', 'h', 'o', and 'n', which combined gives 'Python'.
print(s[0:6:0]) #output: ValueError: slice step cannot be zero, because the step value in slicing cannot be zero. A step value of zero would mean that the slicing operation would not move forward at all, resulting in an infinite loop. Therefore, Python raises a ValueError when you try to use a step value of zero in slicing.
print(s[0:6:-1]) #output:' ', because the slicing operation s[0:6:-1] attempts to extract characters from index 0 to index 5 (6 is exclusive) of the string 'Python' with a step of -1. However, since the step value is negative, it means that the slicing operation would move backward through the string. In this case, it starts at index 0 and tries to move backward, but since there are no characters before index 0, it results in an empty string ''.
print(s[5:0:-1])#ouput: nohty, because the slicing operation s[5:0:-1] extracts characters from index 5 to index 1 (0 is exclusive) of the string 'Python' with a step of -1. This means it retrieves characters in reverse order starting from index 5, resulting in 'n', 'o', 'h', 't', and 'y', which combined gives 'nohty'. Note that index 0 is not included in the result due to the exclusive nature of the end index.
print(s[0:5:-2])#output:' ', because the slicing operation s[0:5:-2] attempts to extract characters from index 0 to index 4 (5 is exclusive) of the string 'Python' with a step of -2. However, since the step value is negative, it means that the slicing operation would move backward through the string. In this case, it starts at index 0 and tries to move backward, but since there are no characters before index 0, it results in an empty string ''.
print(s[5:0:-2])#output: no, because the slicing operation s[5:0:-2] extracts characters from index 5 to index 1 (0 is exclusive) of the string 'Python' with a step of -2. This means it retrieves characters in reverse order starting from index 5, resulting in 'n' and 'o', which combined gives 'no'. Note that index 0 is not included in the result due to the exclusive nature of the end index.
print(s[-6:3:2])#output: Pto, because the slicing operation s[-6:3:2] extracts characters from index -6 to index 2 (3 is exclusive) of the string 'Python' with a step of 2. The negative index -6 refers to the first character of the string, which is 'P'. This means it retrieves every second character starting from index -6, resulting in 'P', 't', and 'o', which combined gives 'Pto'.

"""INDUSTRY EXAMPLE OF SLICING:"""
#1. Extracting a substring from a larger string:
#EX: s="Hello, World!" print(s[7:12]) #output: World

#2.country code from phone number:
#EX: phone_number="+1-123-456-7890" country_code=phone_number[0:2] print(country_code) #output: +1

#3. Extracting a specific portion of a URL:
#EX: url="https://www.example.com/page" domain=url[8:22] print(domain) #output: www.example.com

#4. Extracting a specific portion of a date string:
#EX: date_string="2024-06-15" year=date_string[0:4] month=date_string[5:7] day=date_string[8:10] print(year) #output: 2024 print(month) #output: 06 print(day) #output: 15

#5. Extracting a specific portion of an email address:
#EX: email="john.doe@example.com" username=email[0:8] domain=email[9:20] print(username) #output: john.doe print(domain) #output: example.com

