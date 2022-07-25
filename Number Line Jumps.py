#----------------------------- solution 1-------------------------
# def jump(x1, v1, x2, v2):
#     for _ in range(10000):
#         x1 += v1
#         x2 += v2
#         if x1 == x2:
#             return True
#
#
# x1, v1, x2, v2 = map(int, input().split())
# if x1 < x2 and v1 < v2:
#     print("NO")
# else:
#     if jump(x1, v1, x2, v2):
#         print("YES")
#     else:
#         print("NO")

#--------------------------------- solution 2 ----------------------------------
def kangaroo_jump(x1, v1, x2, v2):
    if x1<x2 and v1<v2:
        return "NO"
    else:
        if v1 != v2 and (x2-x1)%(v2-v1)==0:
            return "YES"
        else:
            return "NO"
x1, v1, x2, v2 = map(int, input().split())
print(kangaroo_jump(x1,v1,x2,v2))