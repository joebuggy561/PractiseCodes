year = int(input("Enter your year of choice?: "))
if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
    print(f"Your year {year}, is a leap year")
else:
    print("Not a leap year")
