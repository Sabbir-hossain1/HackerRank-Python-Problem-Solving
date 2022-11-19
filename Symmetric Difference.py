# You are given two sets of student roll numbers.
# One set has subscribed to the English newspaper,
# and one set has subscribed to the French newspaper. 
# Your task is to find the total number of students
# who have subscribed to either the English or
# the French newspaper but not both.
# input: 
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# output: 8 (The roll numbers of students who have subscriptions to English or French newspapers but not both are:
# 4 5 7 9 10 11 21 55 )

n = input()
set1 = set(map(int,input().rstrip().split()))
n = input()
set2 = set(map(int,input().rstrip().split()))
print(len(set1.symmetric_difference(set2)))