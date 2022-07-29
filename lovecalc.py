print("Welcom to the love calculator")
name1 = input("what is your name?: \n").lower()
name2 = input("what is your name?: \n").lower()

combine_name = name1 + name2


t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")

true = t + r + u + e

l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")

love = l + o + v + e

true_love = int(str(true)+str(love))

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together")
if true_love > 40 and true_love < 50:
    print(f"Your score is {true_love}, you guys are good together")
else:
    (true_love)


