"""
fromat_specifiers={value:flags}format a value based on what flags are interested
for example:
name="John"
print(f"Hello, {name:s}")  # String format
print(f"Hello, {name!r}")  # Representation format
print(f"Hello, {name!a}")  # ASCII format
print(f"Hello, {name:^10s}")  # Centered within 10 spaces"""

# price=49.99
# price1=56.5
# price2=1000.4567
# price3=12.34
# print(f"PRICE IS:{price:.2f}")#Round off to 2 decimal places
# print(f"PRICE IS:{price1:.1f}")#Round off to 1 decimal
# print(f"PRICE IS:{price2:,.2f}")#Comma as thousand separator and round off to 2 decimal places
# print(f"PRICE IS:{price2:0>10.2f}")#Pad with zeros to make total width 10 including decimal places
# print(f"PRICE IS:{price2:<10.2f}")#Left align within 10 spaces
# print(f"price3 is ${price3:10}")#Right align within 10 spaces

price = -4900.99
print(f"PRICE IS:{price:+,.2f}") #output the sign (+/-) along with the number, comma as thousand separator and round off to 2 decimal places
