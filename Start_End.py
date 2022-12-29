import re
S = input()
k = input()
pattern = re.compile(k)
match = pattern.search(S)
if not match:
    print((-1,-1))
else:
    while match:
        start_index = match.start()
        end_index = match.end() -1
        print((start_index,end_index))
        match = pattern.search(S,start_index+1)