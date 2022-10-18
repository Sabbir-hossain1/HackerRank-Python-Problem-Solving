def dynamicArray(n,queries):
    arr = [[] for _ in range(n)]
    lastanswer = 0
    result = []
    for q,x,y in queries:
        if q == 1:
            idx = ((x^lastanswer) % n)
            arr[idx].append(y)
        else:
            idx = ((x^lastanswer)%n)
            lastanswer = arr[idx][y%len(arr[idx])]
            result.append(lastanswer)
    return result

if __name__ == '__main__':
    n,q = list(map(int,input().split()))
    queries = []
    for _ in range(q):
        queries.append(list(map(int,input().rstrip().split())))
    result = dynamicArray(n,queries)
    for value in result:
        print(value)