import random

bankers_names = input("Enter your names here please?: ")
count_banker_names = len(bankers_names.split(","))
# print(count_banker_names)
random_choice = random.randint(0, count_banker_names-1)
print(random_choice)

