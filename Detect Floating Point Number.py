import re
for _ in range(int(input())):
    match = re.search(r"^[+-]?\d*\.\d+$",input())
    if match:
        print(True)
    else:
        print(False)
