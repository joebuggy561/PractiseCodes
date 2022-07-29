print("Welcome to the tip calculator by Stars")
amount = float(input("What is the amnount of the bill?: "))
stars  = int(input("How many stars is the hotel?: "))
people = int(input('How many people will split the bill?: '))

if stars == 1:
    print(amount / people + 0.10)
elif stars == 2:
    print(amount /people + 0.20)
elif stars == 3:
    print(amount / people + 0.30)
elif stars == 4:
    print(amount / people + 0.40)
elif stars == 5:
    print(amount / people + 0.50)
else:
    print("None")

