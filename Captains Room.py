# problem Links: https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
from collections import Counter
n,m = input(),input().split()
for i,j in Counter(m).items():
    if j == 1:
        print(i)

