# Solution 1
# def merge_tools(string, k):
#     ns = ''
#     for i, char in enumerate(string, 1):
#         if char not in ns:
#             ns = ''.join((ns, char))
#         if i % k == 0:
#             print(ns)
#             ns = ''

# Solution 2

def merge_the_tools(string, k):
    for x in range(len(string) // k):
        res = []
        for letter in string[x*k:x*k+k]:
            if letter not in res:
                res.append(letter)
        print(''.join(res))


# s, k = input().split()
# k = int(k)
# splitted_string = []
# for size in range(0, len(s), k):
#     splitted_string.append(s[size:size+k])
# print("initial string", splitted_string)
# for str in splitted_string:
#     print(''.join(set(str)))
# merge_tools('sabbirhossain', 3)
merge_the_tools('sabbirhossain', 3)
