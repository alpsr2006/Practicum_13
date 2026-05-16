from itertools import combinations

numbers = list(map(int, input().split()))
subsets = []
for r in range(len(numbers) + 1):
    for combo in combinations(numbers, r):
        subsets.append(set(combo))

print(subsets)