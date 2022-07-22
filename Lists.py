# -------------------- solution 1 ----------------------

# arr = list()
# for _ in range(int(input())):
#     tasks = input().split()
#     operation = tasks[0]
#     values = tasks[1:]
#     values = list(map(int,values))
#     if operation == "print":
#         print(arr)
#     elif operation == "sort":
#         arr.sort()
#     elif operation == "reverse":
#         arr.reverse()
#     elif operation == "insert":
#         arr.insert(values[0], values[1])
#     elif operation == "remove":
#         arr.remove(values[0])
#     elif operation == "append":
#         arr.append(values[0])
#     elif operation == "pop":
#         arr.pop()

# ------------------------------- solution 2 -------------------------
arr = list()

for _ in range(int(input())):
    user_input = input().split()
    command = user_input.pop(0)
    if len(user_input)> 0:
        if command == "insert":
            eval("arr.{0}({1}){2}".format(command,user_input[0],user_input[1]))
        else:
            eval("arr.{0}({1})".format(command,user_input[0]))
    elif command == "print":
        print(arr)
    else:
        eval("arr.{0}()".format(command))