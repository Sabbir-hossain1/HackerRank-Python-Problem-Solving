# Solution 1
# N,X = input().split()
# Subjects = []
# for i in range(int(X)):
#     Subjects.append(list(map(float,input().split())))
# for avg in zip(*Subjects):
#     print('%.1f' % (sum(avg)/len(avg)))

# Solution 2
# N,X = tuple(map(int,input().split()))
# subjects = (map(float,input().split()) for _ in range(X))
# for student in zip(*subjects):
#     print(round((sum(student)/len(student)),1))

# Solution 3
n,x = map(int,input().split())
for avg in zip(*[map(float,input().split()) for _ in range(x)]):
    print(sum(avg)/x)