# ----------------------------rough solution --------------------------
# def staircase(n):
#     for i in range(1,n+1):
#         for j in range(n-i):
#             print(" ",end="") # 'end="" ' to avoid the new line when print
#         for k in range(i):
#             print("#", end="")
#         print()
# if __name__ == "__main__":
#     n = int(input().strip())
#     staircase(n)
# ----------------------------smart solution 1 -----------------------------
# def staircase(n):
#     num_hash = 1
#     while n > n - n:
#         print((n - 1) * " " + num_hash * "#")
#         n = n - 1
#         num_hash = num_hash + 1
#
#
# if __name__ == "__main__":
#     n = int(input().strip())
#     staircase(n)


# ----------------------------smart solution 2 -----------------------------
def staircase(n):
    for num in range(1, n + 1):
        print(f'{"#" * num:>{n}}')  # '>n' define number of space to right move and '<n' number of space to left move


if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
