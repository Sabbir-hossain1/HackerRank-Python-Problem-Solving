#-------------------------------Tutorial-------------
#  H = set("Hacker")
#  R = set("Rank")
# .intersection_update() or &= : H.intersection_update(R) or H |=R
# .difference_update() or -= : H.difference_update(R) or H -=R
# .symmetric_difference_update() or ^=: H.difference(R) or H ^= R

#-------------------------------------Problem statement------------------
# You are given a set A and N number of other sets.
# These N number of sets have to perform some specific
# mutation operations on set A .
# Your task is to execute those operations and
# print the sum of elements from set A.

# Solution 1
# N = input()
# A = set(map(int,input().rstrip().split()))
# N = int(input())
# for i in range(N):
#     operation = input().split()[0].strip()
#     givenSet = set(map(int,input().rstrip().split()))
#     if operation == 'intersection_update':
#         A.intersection_update(givenSet)
#     elif operation == 'symmetric_difference_update':
#         A.symmetric_difference_update(givenSet)
#     elif operation == 'difference_update':
#         A.difference_update(givenSet)
#     elif operation == 'update':
#         A.update(givenSet)
# print(sum(A))

# Solution 2
_,A = input(),set(map(int,input().split()))

for i in range(int(input())):
    command = str(input().split()[0])
    s = set(map(int,input().split()))
    eval(f"A.{command}({s})")
print(sum(A))