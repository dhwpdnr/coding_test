def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


case = int(input())
arr = list(map(int, input().split()))
count = 0
for i in arr:
    if i == 1:
        pass
    elif is_prime_number(i):
        count += 1
print(count)
