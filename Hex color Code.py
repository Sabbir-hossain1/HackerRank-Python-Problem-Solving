import re
hexCodeList = []
flatList = []
regexp = re.compile("#[a-fA-F0-9]{3,6}")
for _ in range(int(input())):
    hexCodeList.append(regexp.findall(input()))

#flat nested list
for element in hexCodeList:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)

# print hexcode            
for hexcode in flatList:
    print(hexcode)