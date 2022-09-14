# Solution 1
money = 0
x = input()
N = list(map(int,input().split()))
NS = int(input())
for _ in range(NS):
    s,p = list(map(int,input().split()))
    if s in N:
        money +=p
        N.remove(s)
print(money)

# Solution 2

from collections import Counter
number_shoes = int(input())
list_shoe_sizes = Counter(list(map(int,input().split())))
customers = int(input())
total = 0
for i in range(customers):
    customer_size_price = list(map(int,input().split()))
    if list_shoe_sizes[customer_size_price[0]]:
        list_shoe_sizes[customer_size_price[0]] -= 1
        total += customer_size_price[1]
print(total)

