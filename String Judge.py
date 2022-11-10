from collections import Counter
def GoldyString(string):
    fre_list = []
    frequency = Counter(string)
    for val in frequency.values():
        fre_list.append(val)
    fre_list.sort()
    if min(fre_list)==max(fre_list):
        return "YES"
    if ((fre_list[0]+1) == fre_list[1] or (fre_list[0]-1) == fre_list[1]) or (fre_list[len(fre_list)-1]+1) == fre_list[1] or (fre_list[len(fre_list)-1]-1) == fre_list[1]:
        return  "YES"
    else:
        return "NO"


if __name__ == "__main__":
    string = input().rstrip()
    print(GoldyString(string))