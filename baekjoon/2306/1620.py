import sys

n, m = map(int, input().split())

pokemondic_int_key = {}
pokemondic_name_key = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    pokemondic_int_key[i] = name
    pokemondic_name_key[name] = i

for _ in range(m):
    item = sys.stdin.readline().strip()
    if item.isdigit():
        print(pokemondic_int_key[int(item) - 1])
    else:
        print(pokemondic_name_key[item] + 1)
