# Solution 1
# from itertools import combinations_with_replacement
# li=input().split()
# s = ''.join(li[:-1])
# s = sorted(s)
# k = int(li[-1])
# comb = list(combinations_with_replacement(s,k))
# for val in comb:
#     print(''.join(val),sep='\n')

# Solution 2
from itertools import combinations_with_replacement as cwr

li=input().split()
s = list(set(''.join(li[:-1])))
k = int(li[-1])
output = map("".join,cwr(sorted(s),k))
print(*output,sep="\n")