n = int(input())

if n < 2:
    print(set())
else:
    sieve = set(range(2, n))
    for p in range(2, int(n ** 0.5) + 1):
        if p in sieve:
            sieve -= set(range(p * p, n, p))
    print(sieve)