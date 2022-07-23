# --------------- solution 1 ----------
# student_grade = list()
# for _ in range(int(input())):
#     numbers = int(input())
#     if numbers < 38:
#         student_grade.append(numbers)
#     else:
#         remainder = numbers % 5
#         multiple_of_5 = 5 - remainder
#         multiple_five_number = numbers + multiple_of_5
#         if multiple_five_number - numbers < 3:
#             student_grade.append(multiple_five_number)
#         else:
#             student_grade.append(numbers)
#
# for grade in student_grade:
#     print(grade)

# --------------------- solution 2 ---------------------------
student_grade = list()
numbers = list()
for _ in range(int(input())):
    number= int(input())
    numbers.append(number)
student_grade = [i if (i < 38 or i % 5 < 3) else (i + (5 - i % 5)) for i in numbers]

for grade in student_grade:
    print(grade)
