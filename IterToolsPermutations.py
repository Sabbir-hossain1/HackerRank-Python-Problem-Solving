# Solution 1
from itertools import permutations
string,k = input().split()
sorted_string = ''.join(sorted(string))
permuted_string = list(permutations(sorted_string,int(k)))
for iter in permuted_string:
    print(''.join(iter))
    
# Solution 2
from itertools import permutations
s,k = input().split()
perms = list(permutations(sorted(list(s)),int(k)))
print(*[''.join(p) for p in perms],sep='\n')