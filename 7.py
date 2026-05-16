from itertools import permutations

numbers = sorted(map(int, input().split()))
for perm in permutations(numbers):
    print(' '.join(map(str, perm)))