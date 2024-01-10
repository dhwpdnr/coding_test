import math

case = int(input())

lcms = []
gcds = []

for _ in range(case):
    a, b = map(int, input().split())
    lcms.append(math.lcm(a, b))
    gcds.append(math.gcd(a, b))

for k, i in zip(lcms, gcds):
    print(k, i)
