def hourglass(arr):
    maxsum = -99
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            middle = arr[i+1][j+1]
            bottom = sum(arr[i+2][j:j+3])
            total = top+middle+bottom
            maxsum = max(total,maxsum)
    return maxsum
if __name__ == '__main__':
    
    arr = []
    for _ in range(6):
        arr.append(list(map(int,input().rstrip().split())))   
    result = hourglass(arr)
    print(result)


    