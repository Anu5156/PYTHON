#all the string methods
#strings are immutable
b="rohith"
print(b)# rohith
print(id(b)) # 140353441644432
print(type(b)) # <class 'str'>
print(b.capitalize())# Rohith
print(b.upper()) # ROHITH
print(b.lower()) # rohith
print(b.isdigit()) # False
print(b.isalpha()) # True
print(b.isalnum()) # True
print(b.islower()) # True
print(b.isupper()) # False
print(b.endswith("h")) # True
print(b.endswith("H")) # False
print(b.startswith("r")) # True
print(b.startswith("R")) # False
print(b.replace("rohith","Anushka"))# Anushka
print(b) # rohith
##It doesnot replace the original value because strings are immutable(cannot be change)
print(b.split("h")) # ['ro', 'it']
print(b.endswith("h")) # True
print(b.endswith("H")) # False
print(b.startswith("r")) # True
print(b.startswith("R")) # False

str1="HE's name is DAN .He ia an honest man."
print(str1.count("a")) # 4
print(str1.find("DAN")) # 13
print(str1.find("dan")) # -1

str2="We wish you a Marry Christmas\n"
print(str2.isprintable())#false
#since \n is not a printable statement

str3="          " # using spacebar
print(str3.isspace()) # True
str4="  "
print(str4.isspace()) # using tab
#True

#to convert to title case
print(str2.title())#We Wish You A Marry Christmas,(all first letter become capital)

str5="Python is a Interpreted language"
print(str5.swapcase()) #pYTHON IS A iNTERPRETED LANGUAGE


