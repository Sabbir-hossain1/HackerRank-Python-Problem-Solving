# Solution 1
# from collections import OrderedDict
# order_dictionary = OrderedDict()
# 
# N = int(input().rstrip())
# for _ in range(N):
#     item = input().split()
#     item_name = ' '.join(item[:-1])
#     if item_name not in order_dictionary :
#         order_dictionary[item_name] = int(item[-1])
#     else:
#         order_dictionary[item_name] +=int(item[-1])
# for item in order_dictionary:
#     print(item,order_dictionary[item])

# Solution 2
# from collections import OrderedDict
# ordered_dict = OrderedDict()
# n = int(input().rstrip())
# for _ in range(n):
#     item,price = input().rsplit(' ',1)
#     ordered_dict[item] = ordered_dict.get(item,0)+int(price)
#     
# for k,v in ordered_dict.items():
#     print(k,v)

# Solution 3

from collections import OrderedDict
import re

reg = re.compile(r"([A-Z\s]+)\s(\d+)$")
ordered_dict = OrderedDict()

for _ in range(int(input().rstrip())):
    name,price = reg.match(input()).groups()
    ordered_dict[name] = ordered_dict.get(name,0)+int(price)
    
[print(k,v) for k,v in ordered_dict.items()]

