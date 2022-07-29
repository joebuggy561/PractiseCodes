student_score = input("Enter your list of scores?: ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

max_score = 0
for max in student_score:
    if max > max_score:
        max_score = max
print(f"Your max score is; {max_score}")