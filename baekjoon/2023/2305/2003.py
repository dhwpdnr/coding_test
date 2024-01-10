N, M = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 1

count = 0

while (start <= end and end <= N):

    total = sum(arr[start:end])

    if (total < M):
        end += 1

    elif (total > M):
        start += 1

    else:
        count += 1
        end += 1

print(count)
