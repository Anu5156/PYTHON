# # to check the length of the string
# import string #importing string module

# name=input("Enter the name :")
# length=len(name)                                         #output the length of the string ex: Anushka Acharya -> length=15 (including space)
# print(length)
# #to convert to uppercase
# uppercase=name.upper()                                   #output in uppercase   ex: ANUSHKA ACHARYA      
# print(uppercase)
# #to convert to lower case
# lower_case=name.lower()                                 #output in lowercase  ex: anushka acharya
# print(lower_case)
# #to convert to title case
# title_case=name.title()                                #output in titlecase   ex: Anushka Acharya (first letter of each word capital)
# print(title_case) 
# #to convert to capitalize case
# capitalize_case=name.capitalize()                      #output in capitalize case  ex: Anushka acharya (first letter  of the first word capital)
# print(capitalize_case)
# #to check whether the string is alphanumeric
# alphanumeric=name.isalnum()                            #output : True if all characters in the string are alphanumeric (letters and numbers) and there is at least one character, False otherwise.
# print(alphanumeric)
# #to check whether the string is alphabetic
# alphabetic=name.isalpha()                         #output : True if all characters in the string are alphabetic (letters) and there is at least one character, False otherwise.ex: AnushkaAcharya -> True , Anushka Acharya -> False (because of space)
# print(alphabetic)
# #to check whether the string is numeric
# numeric=name.isnumeric()                        #output : True if all characters in the string are numeric and there is at least one character, False otherwise.ex: 12345 -> True , 123a45 -> False
# print(numeric)
# #to check whether the string is in lower case
# lowercase_check=name.islower()                     #output : True if all characters in the string are in lower case and there is at least one character, False otherwise.
# print(lowercase_check)
# #to check whether the string is in upper case
# uppercase_check=name.isupper()                    #output : True if all characters in the string are in upper case and there is at least one character, False otherwise.
# print(uppercase_check)
# #to check whether the string is in title case
# titlecase_check=name.istitle()                    #output : True if the string is in title case, False otherwise. ex: Anushka Acharya -> True , Anushka acharya -> False  
# print(titlecase_check)
# #to check whether the string contains only whitespace
# whitespace_check=name.isspace()
# print(whitespace_check)
# #to strip the whitespace from the string
# stripped_string=name.strip()
# print(stripped_string)
# #to replace a substring with another substring
# replaced_string=name.replace("a","@")
# print(replaced_string)
# #to split the string into a list
# split_string=name.split()
# print(split_string)
# #to join a list into a string
# joined_string="-".join(split_string)
# print(joined_string)
# #to find a substring in the string
# substring_index=name.find("a")
# print(substring_index)
# #to count the occurrences of a substring in the string
# substring_count=name.count("a")
# print(substring_count)
# #to check whether the string starts with a substring
# startswith_check=name.startswith("A")
# print(startswith_check)
# #to check whether the string ends with a substring
# endswith_check=name.endswith("a")
# print(endswith_check)
# #to center the string with a specified width and fill character
# centered_string=name.center(20,"*")
# print(centered_string)
# #to ljust the string with a specified width and fill character
# ljusted_string=name.ljust(20,"-")
# print(ljusted_string)
# #to rjust the string with a specified width and fill character
# rjusted_string=name.rjust(20,"+")
# print(rjusted_string)
# #to zfill the string with a specified width
# zfilled_string=name.zfill(20)
# print(zfilled_string)
# #to translate the string using a translation table
# translation_table=str.maketrans("a","@")
# translated_string=name.translate(translation_table)
# print(translated_string)
# #to check whether the string is printable
# printable_check=name.isprintable()
# print(printable_check)
# #to swap the case of the string
# swapped_case=name.swapcase()
# print(swapped_case)
# #to format the string using f-strings
# formatted_string=f"Hello, {name}!"
# print(formatted_string)
# #to format the string using format() method
# formatted_string2="Hello, {}!".format(name)
# print(formatted_string2)
# #to encode the string to bytes
# encoded_string=name.encode()
# print(encoded_string)
# #to decode the bytes to string
# decoded_string=encoded_string.decode()
# print(decoded_string)
# #to check whether the string is a valid identifier
# identifier_check=name.isidentifier()
# print(identifier_check)
# #to capitalize each word in the string
# capitalized_words=string.capwords(name)
# print(capitalized_words)
# #to expand tabs in the string
# expanded_string="Hello\tWorld".expandtabs(4)
# print(expanded_string)
# #to partition the string into three parts
# partitioned_string=name.partition("a")
# print(partitioned_string)
# #to rpartition the string into three parts
# rpartitioned_string=name.rpartition("a")
# print(rpartitioned_string)
# #to lstrip the string
# lstripped_string="   "+name.lstrip()
# print(lstripped_string)
# #to rstrip the string
# rstripped_string=name+"   ".rstrip()
# print(rstripped_string)
# #to check whether the string is casefolded
# casefolded_check=name.casefold()
# print(casefolded_check)
# #to casefold the string
# casefolded_string=name.casefold()
# print(casefolded_string)
# #to get the ASCII value of a character
# ascii_value=ord(name[0])
# print(ascii_value)
# #to get the character from an ASCII value
# character=chr(ascii_value)
# print(character)
# #to get a list of all ASCII letters
# ascii_letters=string.ascii_letters
# print(ascii_letters)
# #to get a list of all ASCII lowercase letters
# ascii_lowercase=string.ascii_lowercase
# print(ascii_lowercase)
# #to get a list of all ASCII uppercase letters
# ascii_uppercase=string.ascii_uppercase
# print(ascii_uppercase)
# #to get a list of all digits
# digits=string.digits
# print(digits)
# #to get a list of all punctuation characters
# punctuation=string.punctuation
# print(punctuation)
# #to get a list of all printable characters
# printable=string.printable
# print(printable)
# #to get a list of all whitespace characters
# whitespace=string.whitespace
# print(whitespace)
# #to check whether the string is a decimal
# decimal_check=name.isdecimal()
# print(decimal_check)
# #to check whether the string is a float
# def is_float(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False
# #to check whether the string is a digit
# digit_check=name.isdigit()
# print(digit_check)
# #to check whether the string is numeric
# numeric_check=name.isnumeric()
# print(numeric_check)
#to find 

# import string
# name = input("Enter the name :")
# result=name.find(" ")
# print(result)

# #to count how many dashes are there in the string
# # dash_count=name.count("-")

# # print(dash_count)
# replace=name.replace('A','@')
# print(replace)

#TO GET ALL THE STRING METHODS TYPE:
print(help(str))
#-->gets all the methods available for string in python