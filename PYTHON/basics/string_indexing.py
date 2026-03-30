#indexing:accessing elements of a sequence using[].(indexing operator)
#[start:end:step]

credit_number="1234-5678-9876-5432"
# #Accessing individual characters
# first_digit=credit_number[0]
# print(f"First digit:{first_digit}")  #Output: First digit:1
# last_digit=credit_number[-1]
# print(f"Last digit:{last_digit}")    #Output: Last digit:2
# #Slicing substrings
# first_four_digits=credit_number[0:4]
# print(f"First four digits:{first_four_digits}") 
#  #Output: First four digits:1234
# middle_section1=credit_number[5:9]
# print(middle_section1)
#     #Output: Middle section1:5678
# middle_section2=credit_number[10:14]
# print(middle_section2)
#     #Output: Middle section2:9876

# last_four_digits=credit_number[-4:]
# print(f"Last four digits:{last_four_digits}")
# #Output: Last four digits:5432
#Using step in slicing
# every_second_digit=credit_number[::2]
# print(f"Every second digit:{every_second_digit}")

""" printing the last digit to the first digit in reverse order"""
reverse_order=credit_number[::-1]
print(f"Credit number in reverse order:{reverse_order}")
# Output: Credit number in reverse order:2345-6789-8765-4321

"""printing in the format of XXXX-XXXX-XXXX-5432"""
formatted_number="XXXX-XXXX-XXXX-"+credit_number[-4:]
print(f"Formatted credit number:{formatted_number}")