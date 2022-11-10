n = int(input().rstrip())
country = set()
for _ in range(n):
    country.add(input().rstrip())
print(len(country))