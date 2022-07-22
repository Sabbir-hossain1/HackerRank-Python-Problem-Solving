#------------------ solution 1 -------------------
# student_list = list()
# total_mark = 0
# avg = 0
# for _ in range(int(input())):
#     student_list.append(input().strip().split())
# # print(student_list)
# query_names = input()
#
# for student in student_list:
#     if student[0] == query_names:
#         for i in range(1, len(student)):
#             total_mark += float(student[i])
#         print("%.2f"%(total_mark/ (len(student)-1)))
# ------------------------------- solution 2 using dictionary ----------------------

students = dict()
for _ in range(int(input())):
    student = input().split()
    name,*marks = student
    marks = list(map(float,marks))
    students[name] = marks
query_names = input()

if query_names in students:
    print("%.2f" % (sum(students[query_names])/len(students[query_names])))

