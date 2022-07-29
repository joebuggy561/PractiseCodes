
import random

rock = print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

scissors = print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')



# while True:

# choice_list = rock, paper, scissors

user  = int(input("Enter your choice; 'rock = 0','paper = 1','scissors = 2'?: \n"))
print(f"your choice is {user}")
computer = random.randint(0,2)
print(f"computer choice is {computer}")

if (user == computer):
    print("its a tie")
elif (user == 0 and computer == 2):
    print("you win")
elif (user == 2 and computer == 1):
    print("you win")
elif (user == 1 and computer == 0):
    print("you win")
else:
    print("you loose")