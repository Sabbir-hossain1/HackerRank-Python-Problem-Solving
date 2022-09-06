# solution 1

# def caritsian_product(arr1,arr2):
#     for i in arr1:
#         for j in arr2:
#             print((i,j),end="")
            
            
# Solution 2
# from itertools import product
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# p = list(product(a,b))
# for i in range(len(p)):
#     print(p[i],end='')


# Solution 3

from itertools import product
arr1 = set(map(int,input().split()))
arr2 = set(map(int,input().split()))
print(*list(product(arr1,arr2)))


# if __name__ == "__main__":
#     arr1 = [1,2,3]
#     arr2 = [5,6,7]
#     caritsian_product(arr1,arr2)