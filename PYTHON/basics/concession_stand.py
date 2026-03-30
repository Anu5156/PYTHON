#concessions are sold at a stand they are stored in a dictionary with their prices:
# for example menue card
menu = {"popcorn......":"$5.00",
        "soda.........":"$3.00",
        "candy........":"$2.50",
        "hot dog......":"$4.00",
        "nachos.......":"$4.50"
    }
for item in menu:
    print(f"{item} {menu[item]}")
# Now imagine a customer comes to the stand and orders a soda and a hot dog.

order = ["soda", "hot dog"]
total = 0.0
for item in order:
    price = float(menu[item].strip("$"))
    total += price
print(f"Your total is: ${total:.2f}")
