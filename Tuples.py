# solution 1

# n = int(input())
# integers = map(int,input().split())
# t = tuple(integers)
# print(hash(t))

# solution 2
n = input()
print(hash(tuple(map(int, input().strip().split(" ")))))
