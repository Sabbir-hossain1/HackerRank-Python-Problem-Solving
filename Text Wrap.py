import textwrap
string, break_num = input(), int(input())
desire_string = textwrap.fill(string,break_num)
print(desire_string)