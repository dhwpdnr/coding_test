case = int(input())
candies = []
rests = []
for _ in range(case):
    candy, children = map(int, input().split())
    a, b = divmod(candy, children)
    candies.append(a)
    rests.append(b)
for candy, rest in zip(candies, rests):
    print(f"You get {candy} piece(s) and your dad gets {rest} piece(s).")
