from numpy import average


student_heights = input("Enter a list of students heights?: ").split()
# print(student_heights)
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

total_count = 0
for count in student_heights:
    total_count += 1
print(total_count)

average_height = total_height/total_count
print(average_height)