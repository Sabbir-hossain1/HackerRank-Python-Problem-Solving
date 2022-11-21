for _ in range(int(input())):
    n , A = input(),set(map(int,input().rstrip().split()))
    m ,B = input(),set(map(int,input().rstrip().split()))
    print(A.issubset(B))
    