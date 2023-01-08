# Solution 1
import re
roman = input()
if re.search(r"^(I|V|C|D|L|M|X)+$",roman) == None:
    print(False)
elif re.search(r"(IIII|XXXX|CCCC|MMMM|VV|LL|DD)",roman) != None:
    print(False)
else:
    print(True)

# Solution 2
thousand = 'M{0,3}'
hundred = 'C[MD]|D?C{0,3}'
ten = 'X[CL]|L?X{0,3}'
digit = 'I[VX]|V?I{0,3}'
regex_pattern = r"%s%s%s%s$" % (thousand,hundred,ten,digit)
print(regex_pattern)
print(str(bool(re.match(regex_pattern,input()))))