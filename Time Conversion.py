# return_time = ""
# time_string = input().split(':')
# if "P" in time_string[-1] and int(time_string[0]) <12:
#     time_string[0] = str(int(time_string[0]) + 12)
#     for item in time_string:
#         return_time +=f"{item}:"
#     print(return_time[:-1])
# elif "A" in time_string[-1] and int(time_string[0])  == 12:
#     time_string[0] = '00'
#     for item in time_string:
#         return_time +=f"{item}:"
#     print(return_time[:-1])

time = input().strip()
h, m, s = map(int, time[:-2].split(':'))
p = time[-2:]
h = h % 12 + (p.upper() == 'PM') * 12
print(('%02d:%02d:%02d') % (h, m, s))