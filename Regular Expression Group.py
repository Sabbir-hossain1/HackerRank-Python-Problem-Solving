# Solution 1
# import re
# m = re.search(r"([a-z0-9])\1{1,}",input())
# print(m.group()[0]) if m else print(-1)

# Solution 2
import re
match = re.search(r"([A-Za-z\d])(?=\1)",input())
print(match[0] if match else -1)