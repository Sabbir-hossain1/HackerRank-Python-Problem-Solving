
# Read four numbers,a ,b c,d , and , and print the result of a^b + c^d
# Solution 1
import sys
a,b,c,d = map(int,sys.stdin)
print(pow(a,b)+pow(c,d))

# Solution 2

a,b,c,d = int(input()),int(input()), int(input()),int(input())
print(a**b+c**d)