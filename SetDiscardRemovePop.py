# Solution 1
# n,s = int(input()),set(map(int, input().split()))
# for _ in range(int(input())):
#     li = input().split()    
#     if li[0]=='remove' or li[0]=='discard':
#         s.discard(int(li[1]))
#     else:
#         s.pop()
# print(sum(s))

# Solution 2
# n,s = int(input()),set(map(int,input().split()))
# for _ in range(int(input().rstrip())):
#     cmd,*args = input().split()
#     args=map(int,args)
#     eval(f"s.{cmd}(*args)")
# print(sum(s))

#Solution 3
n,s = int(input()),set(map(int,input().split()))
for _ in range(int(input().rstrip())):
    line = input().split()
    command = line[0]
    value = '' if len(line)<=1 else line[1]
    eval(f"s.{command}({value})")
print(sum(s))

