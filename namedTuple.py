# # Normal Solution 
# from collections import namedtuple
# if __name__ == "__main__":
#     student_list = []
#     n = int(input().rstrip())
#     columns = input().rstrip().split()
#     Student = namedtuple('Student',columns)
#     for i in range(n):
#         student_list.append(Student(*input().rstrip().split()))
#     
#     print(round((sum([int(value.MARKS) for value in student_list])/n),2))

# Solution  1 in 4 lines
# from collections import namedtuple
# n, Table = int(input()), namedtuple("Table",input())
# print(round(sum(int(Table(*input().split()).MARKS) for _ in range(n))/n,2))

# Solution 2 in 4 lines
from collections import namedtuple
n = int(input().rstrip())
data = namedtuple("Data",input().rstrip().split())
print(round(sum([int(data._make(input().rstrip().split())._asdict()['MARKS']) for _ in range(n)])/n,2))
