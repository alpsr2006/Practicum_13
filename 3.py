sladkoezhkin = set(input().split())
n = int(input())
friends = [set(input().split()) for _ in range(n)]

friends_union = set.union(*friends) if friends else set()
only_sladkoezhkin = sladkoezhkin - friends_union
print(len(only_sladkoezhkin))