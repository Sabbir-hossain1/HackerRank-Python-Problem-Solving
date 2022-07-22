# ------------------- solution 1--------------------
# integer_list = list(map(int,input().split()))
# integer_list.sort()
# max_sum = sum(integer_list[1:])
# min_sum = sum(integer_list[:-1])
# print(f"{min_sum} {max_sum}")

# ---------------------- soution 2 ----------------
integer_list = list(map(int,input().split()))
total = sum(integer_list)
print(f"{total- max(integer_list)} { total- min(integer_list)}")