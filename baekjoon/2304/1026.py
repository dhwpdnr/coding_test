case = int(input())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort(reverse=True)
arr_b.sort()

answer = 0
for a, b in zip(arr_a, arr_b):
    answer += a * b

print(answer)
