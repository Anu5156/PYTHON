# task1

#Anushka: wherever there is 'a' replace with @
name="anushka"
for ch in name:
    if ch=="a":
        print("@", end="")
    else:
        print(ch, end="")
#output: @nushk@, because the loop iterates through each character in the string "anushka" and checks if it is equal to "a". If it is, it prints "@", otherwise it prints the character itself. The end parameter in the print function is set to an empty string, so all the characters are printed on the same line without any spaces in between.


print("anushka", end="@")
#output: anushka@, because the end parameter in the print function specifies what should be printed at the end of the output. By default, it is a newline character (\n), but in this case, it is set to "@", so the output will be "anushka@" instead of "anushka\n".

print("anushka", end=" ")
print("acharya")
#output: anushka acharya, because the first print statement prints "anushka" with a space at the end, and the second print statement prints "acharya" immediately after it on the same line.

print("hello","python","!!",sep="@@")
#output: hello@@python@@!!, because the sep parameter in the print function specifies what should be printed between the arguments. By default, it is a space character, but in this case, it is set to "@@", so the output will be "hello@@python@@!!" instead of "hello python !!".

