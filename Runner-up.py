# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int,input().split()))
#     arr.sort(reverse=True)
#     # print(arr)
#     max = max(arr)
#     for item in arr:
#         if item < max:
#             print(item)
#             break

# ----------------------smart solution 1 ---------------------------------


# if __name__ == "__main__":
#     n = int(input())
#     arr = map(int,input().split())
#     print(sorted(list(set(arr)))[-2])


# ----------------------smart solution 2 ---------------------------------
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))[:n] # restrict input only n numbers
    print(sorted(list(set(arr)))[-2])

