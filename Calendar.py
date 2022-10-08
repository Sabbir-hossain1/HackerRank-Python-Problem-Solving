from calendar import day_name,weekday
m,d,y = map(int,input().split())
day = day_name[weekday(y,m,d)].upper()
print(day)
