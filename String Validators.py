# solution 1
# input_string = input()
# alnum = False
# alpha = False
# digits = False
# lower = False
# upper = False
# for letter in input_string:
#     if letter.isupper():
#         upper = True
#     if letter.islower():
#         lower = True
#     if letter.isdigit():
#         digits = True
#     if letter.isalnum():
#         alnum = True
#     if letter.isalpha():
#         alpha = True
# print(alnum)
# print(alpha)
# print(digits)
# print(lower)
# print(upper)

# solution 2


# print(any(c.isalnum() for c in str))
# print(any(c.isalpha() for c in str))
# print(any(c.isdigit() for c in str))
# print(any(c.islower() for c in str))
# print(any(c.isupper() for c in str))


#solution 3

str = input()
for test in ('isalnum','isalpha','isdigit','islower','isupper'):
    print(any(eval("c."+test+"()") for c in str))
