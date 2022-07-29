print("Welcome to pizza deliveries")
size = input("What size pizza do you want? S, M, L: ").lower()
add_peproni = input("Do you want peperoni? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
bill = 0

if size == "s":
    bill  += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
if add_peproni == "y":
    if size == "y":
        bill += 2
    else:
        bill += 3
if extra_cheese == "y":
    bill += 1

if bill > 15:
    add_delivery_pay = bill + 0.10
print(bill)