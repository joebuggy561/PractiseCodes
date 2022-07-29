height = float(input("What is your height?: "))
weight = float(input("What is your weight?: "))
bmi = weight/height ** 2

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are under weight")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your bmi is {bmi}, you are normal weight")
elif bmi >25 and bmi <= 30:
    print(f"Your bmi is {bmi}, you are over weight")
elif bmi >30 and bmi <= 35:
    print(f"Your bmi is {bmi}, you are obese")
elif bmi > 35:
    print(f"You bmi  is {bmi}, you are clinically obese")
else:
    print("start again")