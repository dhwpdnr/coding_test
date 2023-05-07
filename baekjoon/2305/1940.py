n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
start, end = 0, n - 1
while start < end:
    if arr[start] + arr[end] == m:
        answer += 1
        start += 1
        end -= 1
    elif arr[start] + arr[end] < m:
        start += 1
    else:
        end -= 1

print(answer)
