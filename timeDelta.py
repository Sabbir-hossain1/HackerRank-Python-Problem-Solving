from datetime import datetime
for t in range(int(input())):
    a = datetime.strptime(input(),"%a %d %b %Y %X %z")
    b = datetime.strptime(input(),"%a %d %b %Y %X %z")
    return str(abs(int((a-b).total_seconds())))