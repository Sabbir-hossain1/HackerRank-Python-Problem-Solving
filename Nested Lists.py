# Basic discussion about list

# nested_list = [['sabbir', '10'], ['salman', '12'], ['sam', '30']]
# print(nested_list[1])    # output: ['salman', '12']
# print(nested_list[2][0]) # output: 'sabbir'
# print(nested_list[2][1]) # output: '30'

# nested_list = [['sabbir', '10'], ['salman', '12'], ['sam', '30']]
# for single_list in nested_list:
#     for value in single_list:
#         print(value)
#     print()


# students = []
# for _ in range(int(input())):
#     students.append([input(),float(input())])

#--------------------Rough-------------------------

# students = [['aziz', 90.0], ['sahriar', 110.0], ['harun', 80.0], ['shohel', 90.0], ['sabbir', 90.0],["kabir",80.0]]
#
# students.sort(key= lambda x:x[1])
# # sorted(students,key=lambda x:x[1],reverse=False)
#
# second_lowest = students[1]
# first_number = students[0]
# length = len(students)
# for i in range(1, length):
#     if first_number[1] == students[i][1]:
#         students.remove(students[i])
#         length = length - 1
# second_lowest_list = []
# second_lowest_list.append(second_lowest)
#
# for i in range(2,len(students)):
#     if second_lowest[1] == students[i][1]:
#         second_lowest_list.append(students[i])
#
# second_lowest_list.sort(key=lambda x:x[0])
# for names in second_lowest_list:
#     print(names[0])

# -------------------------------solution using list----------------------
# students = []
# for _ in range(int(input())):
#     students.append([input(), float(input())])
# students.sort(key=lambda x:x[1])
#
# student_from_second = [student for student in students if student[0] != students[0][0]]
# second_lowest_student = [student for student in student_from_second if student[1] == student_from_second[0][1]]
# second_lowest_student.sort()
#
# for names in second_lowest_student:
#     print(names[0])

#------------------------------------ solution using dictionary -----------------------
d = {}
for _ in range(int(input())):
    name = input()
    grade = float(input())
    d[name] = grade
values = d.values()
second = sorted(list(set(values)))[1]
second_lowest = []
for key, value in d.items():
    if value == second:
        second_lowest.append(key)
second_lowest.sort()

for name in second_lowest:
    print(name)




