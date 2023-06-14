def gcd(a, b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a


n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

a = eval("*".join(map(str, arr1)))
b = eval("*".join(map(str, arr2)))

print('%s' % str(gcd(a, b))[-9:])
