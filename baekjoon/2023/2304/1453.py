case = int(input())

numbers = list(map(int, input().split()))

set_num = set(numbers)

print(len(numbers) - len(set_num))
