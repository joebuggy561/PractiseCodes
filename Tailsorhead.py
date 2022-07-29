import random

choose = input("Please make a choice 0 or 1 ?: ")
choosen = int(choose)
random_choice = random.randint(0, choosen)

if random_choice == 1:
    print(f"{random_choice} you choose head")
elif random_choice == 0:
    print(f"{random_choice} you choose tails")
else:
    print("wrong choice try again")