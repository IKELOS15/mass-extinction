grading = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", 'F']
mor = [4.5, 4.0, 3.0, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
total_grade = float(0.0)
total_num = float(0.0)


for i in range(20):
    subject, num, grade = input().split()

    if grade == "P" or "N" :
        continue
    else:
        for i in range(len(grading)):
            if grade == grading[i]:
                grade = mor[i]
        total_grade += float(num * grade)
        total_num += float(num)


if total_num != 0.0:
      print(total_grade / total_num)


"""ObjectOrientedProgramming1 3.0 A+
ProblemSolving 4.0 P
"""
