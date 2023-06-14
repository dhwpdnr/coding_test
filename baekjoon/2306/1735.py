def gcd(a, b):
    while a % b != 0:
        mod = a % b
        a = b
        b = mod
    return b


a, b = map(int, input().split())
c, d = map(int, input().split())

g1 = gcd(b, d)
demon = b * d // g1
mole = a * (d // g1) + c * (b // g1)

g2 = gcd(demon, mole)
print(mole // g2, demon // g2)
