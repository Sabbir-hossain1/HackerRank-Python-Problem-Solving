# -------------------------- Tutorial--------------
# from collections import deque
# d = deque()
# d.append(1) # deque(['1'])
# d.appendleft(2) # deque(['1','2'])
# d.clear() # deque([])
# d.extend('1') # deque(['1'])
# d.extendleft('234') # deque(['4','3','2','1'])
# print(d)
# d.pop() # deque(['4','3','2'])
# print(d)
# d.popleft()  # deque(['3','2'])
# print(d)
# d.extend('7896') # deque(['3', '2', '7', '8', '9', '6'])
# print(d)
# d.remove('2') # deque(['3', '7', '8', '9', '6'])
# print(d)
# d.reverse() # deque(['6', '9', '8', '7', '3'])
# print(d)
# d.rotate(2) # deque(['7', '3', '6', '9', '8'])
# print(d)

# ---------------------- problem statement ------------------
# Perform append, pop, popleft and appendleft methods on an empty deque .

#------------------ input:--------------
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# -----------------output-----------
# 1 2

# Solution 1
# from collections import deque
# d = deque()
# for _ in range(int(input())):
#     operations,*args = input().split()
#     getattr(d,operations)(*args)
# print(*d)

# solution 2
from collections import deque
d = deque()
for i in range(int(input())):
    x,*y=input().split()
    eval(f"d.{x} (*y)")
print(*d)
    