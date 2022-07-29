# number = input("Enter your list of numbers?: ").split()
# for n in range(0, len(number)):
#     number[n] = int(number[0])
#     print(number)

addEvennum = 0
for num in range(2, 101, 2):
    addEvennum += num

print(f"Added even num {addEvennum}")