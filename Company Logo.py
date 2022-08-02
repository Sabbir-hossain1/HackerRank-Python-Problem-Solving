# scratch solution
# count_each_letter = {}
# input_string = input()
# input_string_list = [s for s in input_string] list[:0] = input_string
#
# for value in input_string_list:
#     count_each_letter[value] = 0
# for value in input_string_list:
#     count_each_letter[value] += 1
# count_each_letter = sorted(count_each_letter.items(),key=lambda x: x[1],reverse= True)
#
# for item in count_each_letter:
#     print(item[0],item[1])


# from collections import Counter
# s = input()
# frequency = Counter((s))
# for k, v in frequency.most_common(3):
#     print(k,v)

Dict = {}
string_list = []
s = input()
string_list[:0] = s
string_list = sorted(string_list)
for x in string_list:
    Dict[x] = string_list.count(x)
sorted_list = sorted(Dict.items(), key=lambda x: x[1], reverse=True)
for item in sorted_list[:3]:
    print(item[0],item[1])
