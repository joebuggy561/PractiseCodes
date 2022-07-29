print("Welcome to the tip calculator by Stars")
amount = float(input("What is the amnount of the bill?: "))
tip  = int(input("How much to do you want to leave?: "))
people = int(input('How many people will split the bill?: '))
tip_in_percentage = tip / 100
amount_bill_per_person = amount / people + tip_in_percentage
final_amount_in_2f = round(amount_bill_per_person, 2)
print(final_amount_in_2f)