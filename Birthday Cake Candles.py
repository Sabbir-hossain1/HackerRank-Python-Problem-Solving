# ------------- solution 1 -----------
# N = input()
# count = 0
# candle_height = list(map(int, input().strip().split()))
# tallest_value = max(candle_height)
# for value in candle_height:
#     if value>= tallest_value:
#         count += 1
# print(count)

# ------------------- solution 2-----------
n = input()
candle_height = list(map(int, input().strip().split()))
print(candle_height.count(max(candle_height)))