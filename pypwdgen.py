import random

Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+"]

print("Welcom to my password Generator")

no_letters = int(input("How many letters will you like in you password?: \n"))
no_numbers = int(input("How many numbers will you like in you pass word btween 1-10?: \n"))
no_symbols = int(input("How many symbols will you like in your password?: \n"))

password = ""
for char in range(1, no_letters + 1):
   password += random.choice(Letters)

for char in range(1, no_numbers + 1):
    password += random.choice(numbers)

for char in range (1, no_symbols):
    password += random.choice(symbols)


print(password)