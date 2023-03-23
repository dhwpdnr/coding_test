def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


min_num = int(input())
max_num = int(input())
answer = []
for num in range(min_num, max_num + 1):
    if num > 1:
        if is_prime_number(num):
            answer.append(num)
if len(answer) > 0:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)
