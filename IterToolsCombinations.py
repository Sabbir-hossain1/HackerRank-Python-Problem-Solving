# solution 1

# from itertools import combinations
# string,k = input().split()
# string = sorted(string)
# k = int(k)
# for i in range(1,k+1):    
#     comb = list(combinations(string,i))
#     for v in comb:
#         print(*v,sep='')

# Solution 2
from itertools import combinations
string,k = input().split()
string = sorted(string)
k = int(k)
for i in range(1,k+1):
    for j in combinations(string,i):
        print("".join(j))