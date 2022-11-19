# find set intersection : like some people subcribe to english newspaper
# and some for french find the number of people who subcribe to both
# intput: 1 2 3 4 5 6 7 8 9    and 
#         10 1 2 3 11 21 55 6 8 
# output: 5(1,2,3,6,8) students is subscribe to both 

# Solution 1
n = input()
set1 = set(map(int,input().rstrip().split()))
m = input()
set2 = set(map(int,input().rstrip().split()))
count = set1.intersection(set2)
print(len(count))

# print(len(set1.intersection(set2)))
