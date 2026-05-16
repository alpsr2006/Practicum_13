from itertools import combinations

numbers = list(map(int, input().split()))
k = int(input())

k_subsets = [set(combo) for combo in combinations(numbers, k)]
print(k_subsets)