string = input()
position,value = input().split()
print(string[:int(position)]+value+string[int(position)+1:])
