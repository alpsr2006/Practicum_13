n = int(input())
courses_sets = [set(input().split()) for _ in range(n)]

common_courses = set.intersection(*courses_sets)
print(len(common_courses))