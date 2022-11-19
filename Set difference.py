# You are given two sets of student roll numbers.
# One set has subscribed to the English newspaper,
# and one set has subscribed to the French newspaper.
# Your task is to find the total number of students 
# who have subscribed to only English newspapers.
# input: 
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# Output: 4
n = input()
set1 = set(map(int,input().rstrip().split()))
n = input()
set2 = set(map(int,input().rstrip().split()))
print(len(set1.difference(set2)))

