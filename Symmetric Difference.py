# solution 1
# symmetric_diff = []
# m = int(input().rstrip())
# a = set(map(int,input().rstrip().split()))
# n = input().rstrip()
# b = set(map(int,input().rstrip().split()))
# 
# intersect = a.intersection(b)
# a = a.difference(intersect)
# b = b.difference(intersect)
# symmetric_diff = list(a.union(b))
# symmetric_diff.sort()
# for value in symmetric_diff:
#     print(value)

# Solution 2

# m = int(input())
# a = set(map(int,input().split()))
# n = int(input())
# b = set(map(int,input().split()))
# print(*sorted(a^b),sep='\n')

# Solution 3

m = int(input().rstrip())
a = set(map(int,input().split()))
n = int(input().rstrip())
b = set(map(int,input().split()))
print(*sorted(a.symmetric_difference(b)),sep='\n')
