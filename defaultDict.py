from collections import defaultdict

#Normal Checking frequency of a string

# name = "sabbir hossain"
# d = {}
# for l in name:
#     if l not in d:
#         d[l] = 1
#     else:
#         d[l] += 1
# print(d)

# Checking Frequency of a string with defaultdict
# d = defaultdict(int)
# name = "sabbir hossain"
# for l in name:
#     d[l] +=1
#     
# print(d)


# d = defaultdict(lambda: "not Present")
# d['a'] = 1
# d['b'] = 2
# 
# print(d['a'])
# print(d['b'])
# print(d['d'])


# d = defaultdict(list)
# 
# d['a'].append(5)
# d['b'].append(6)
# d['a'].append(7)
# print(d)
  
  
# # Defining a dict
# d = defaultdict(list)
#   
# for i in range(5):
#     d[i].append(i)
#       
# print("Dictionary with values as list:")
# print(d)

# d = defaultdict(int)
# L = [1, 2, 3, 4, 2, 4, 1, 2]
# 
# for i in L:
#     d[i] += 1
# print(d)
# print(d[4])


# Hacker rank Problem solving DefaultDict

# from collections import defaultdict
# 
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)

# Solution 1

# A = []
# B = []
# m,n = map(int,input().split())
# for _ in range(m):
#     A.append(input())
# for _ in range(n):
#     B.append(input())
# for i in B:
#     negative_index = True
#     for index,l in enumerate(A):
#         if l == i:
#             negative_index = False
#             print(index+1,end=" ")
#     if negative_index:
#         print('-1')
#     print('')

# Solution 2

n,m = map(int,input().split())
d = defaultdict(list)
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    x = input()
    if x in d:
        print(*d[x])
    else:
        print('-1')

