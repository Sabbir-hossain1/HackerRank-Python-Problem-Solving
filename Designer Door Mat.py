# solution 1
# n,m = map(int,input().split())
# c = ".|."
# j=1
# k=0
# for i in range(1,n):
#     if k==0:
#         print((c*j).center(m,"-"))
#         j+=2
#         if int(n/2) == i:
#             print("WELCOME".center(m,"-"))
#             k = j
#     else:
#         k = k-2
#         print((c*k).center(m,"-"))


# slution 2
N,M = map(int,input().split())
for i in range(1,N,2):
    print((i*".|.").center(M,"-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2):
    print((i*".|.").center(M,"-"))
