raw1 = ["", "","",]
raw2 = ["", "","",]
raw3 = ["", "","",]

map = [raw1, raw2, raw3]

position = input("Enter the postion of the treasure?: ")

horizontal = int(position[0])
vertical = int(position[1])

select_row = map[vertical -1]
select_row[horizontal -1] = "x"

print(f"{raw1}\n{raw2}\n{raw3}")