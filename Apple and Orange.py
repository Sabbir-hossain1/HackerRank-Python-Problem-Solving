#------------------- solution 1 --------------------
# house_start, house_end = map(int, input().split())
# apple_tree, orange_tree = map(int, input().split())
# number_of_apple, number_of_orange = map(int, input().split())
# apple_distance = list(map(int, input().split()))
# orange_distance = list(map(int, input().split()))
#
# apple_count = 0
# orange_count = 0
#
# for distance in apple_distance:
#     if house_start <= apple_tree + distance <= house_end:
#         apple_count += 1
# for distance in orange_distance:
#     if house_start <= orange_tree + distance <= house_end:
#         orange_count += 1
# print(apple_count)
# print(orange_count)

# ---------------------- solution 2----------------------
# house_start, house_end = map(int, input().split())
# apple_tree, orange_tree = map(int, input().split())
# number_of_apple, number_of_orange = map(int, input().split())
# apple_distance = list(map(int, input().split()))
# orange_distance = list(map(int, input().split()))

# print(sum([1 for x in apple_distance if house_start<=apple_tree+x <= house_end]))
# print(sum([1 for x in orange_distance if house_start<=orange_tree+x <= house_end]))

# print(sum(house_start<=apple_tree+distance<=house_end for distance in apple_distance)) # True = 1
# print(sum(house_start<=orange_tree+distance<=house_end for distance in orange_distance)) # False = 0

# ---------------- solution 3 ------------------------------
s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
print(sum([s<=a+int(d)<=t for d in input().strip().split()]))
print(sum([s<=b+int(d)<=t for d in input().strip().split()]))
