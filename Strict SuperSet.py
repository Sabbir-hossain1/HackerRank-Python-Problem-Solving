#-----------------problem statement-------------------
# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.
# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
# A strict superset has at least one element that does not exist in its subset.
#--------------------------input-----------------------------------
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
#--------------------Output----------------------
# False

#Solution 1
A = set(map(int,input().split()))
n = int(input())
c = 0
for _ in range(n):
    B = set(map(int,input().split()))
    if (B.issubset(A) and len(A)>len(B)):
       c = c+1
if c == n:
    print(True)
else:
    print(False)

# Solution 2
A = set(map(int,input().split()))
result = True
for _ in range(int(input())):
    B = set(map(int,input().split()))
    if not (B.issubset(A) and len(A)>len(B)):
        result = False
print(result)

# Solution 3
A = set(map(int, input().split()))
for _ in range(int(input())):
    val = A.issuperset(set(map(int,input().split())))
    if val == False:
        break
print(val)

# Solution 4

A = set(map(int,input().split()))
B = [set(map(int,input().split())) for _ in range(int(input()))]
print(all([A.issuperset(b) and len(A)>len(b) for b in B]))