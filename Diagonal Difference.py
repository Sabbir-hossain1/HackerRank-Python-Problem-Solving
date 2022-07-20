

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.



def diagonalDifference(arr):
    # Write your code here
    diff1 = sum([arr[x][x] for x in range(0, len(arr))])
    diff2 = sum([arr[x][len(arr) - 1 - x] for x in range(0, len(arr))])
    return abs(diff1 - diff2)

    # if __name__ == '__main__':
    #     fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input("enter the n : ").strip())

arr = []

for index in range(n):
    arr.append(list(map(int, input(f"Enter the row no {index}: ").rstrip().split())))

result = diagonalDifference(arr)
print(result)

