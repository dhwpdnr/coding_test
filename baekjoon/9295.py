case = int(input())
dice_sum = []
for _ in range(case):
    a, b = map(int, input().split())
    dice_sum.append(a + b)
for index, num in enumerate(dice_sum):
    print(f"Case {index + 1}: {num}")
