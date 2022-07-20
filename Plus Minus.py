# --------------------------rough solution--------------------------#

# def plusMinus(arr):
#     # Write your code here
#     positive_count = 0
#     negative_count = 0
#     zero_count = 0
#     for n in arr:
#         if n > 0:
#             positive_count += 1
#         elif n < 0:
#             negative_count += 1
#         else:
#             zero_count += 1
#     size_of_array = len(arr)
#     positive_ratio = positive_count / size_of_array
#     negative_ratio = negative_count / size_of_array
#     zero_ratio = zero_count / size_of_array
#
#     print("%.6f" % positive_ratio)
#     print("%.6f" % negative_ratio)
#     print("%.6f" % zero_ratio)

# ---------------------------Smart solution 1-------------------------------
# def plusMinus(arr):
#     n = len(arr)
#     print(format(len([x for x in arr if x > 0])/n,".6f"))
#     print(format(len([x for x in arr if x < 0])/n,".6f"))
#     print(format(len([x for x in arr if x == 0])/n,".6f"))

# -----------------------smart solution 2---------------------------
def plusMinus(arr):
    n = len(arr)
    print("%.6f" % (len(list(filter(lambda num: num > 0, arr))) / n))
    print("%.6f" % (len(list(filter(lambda num: num < 0, arr)))/ n))
    print("%.6f" % (len(list(filter(lambda num: num == 0, arr)))/ n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
