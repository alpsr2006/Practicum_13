set1 = set(input().split())
set2 = set(input().split())
value = input().strip()

intersection = set1 & set2

if value in intersection:
    print("Yes")
else:
    print("No")