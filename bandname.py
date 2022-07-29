#import the library, writer, split, random, result, csv

from csv import writer
from posixpath import split
import random
import string
from unittest import result
import csv



#define you variable and split
    
print("Welcome to the bandname generator")
city = list(input("Which city did you grow up in?: \n"))
petname = list(input("What is your pet name?: \n"))
name = (city + petname)
letters = [word for word in name[0:]]
print(letters)


# make funtions for parametrs for return split letters
def bandnames():
    randomNumber = random.randint(2, 10)
    print(randomNumber)
    name2 = " "

#for loop to  loop through split and select letters at random
    for x in range(randomNumber):
        randomletters = random.choice(letters)
        name2 = name2 + randomletters
    return name2
# to check if the code is running print("This is your bandname", bandnames())

# write funtion to help create multiple csv file, where it a(append) first try with 'w' before input the a when making another for loop for iteration of csv list
def writecsv():
    with open('name.csv', 'a') as file:
        writer = csv.writer(file)
        name = bandnames()
        writer.writerow([name])
for i in range(10):
    writecsv()