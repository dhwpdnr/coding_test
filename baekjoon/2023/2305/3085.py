# 풀이 참조

case = int(input())
arr = [list(input()) for _ in range(case)]
answer = 0


def check(arr):
    value = 1
    for i in range(case):
        count = 1
        for j in range(1, case):
            if arr[i][j] == arr[i][j - 1]:
                count += 1
            else:
                count = 1

            if count > value:
                value = count

        count = 1
        for j in range(1, case):
            if arr[j][i] == arr[j - 1][i]:
                count += 1
            else:
                count = 1

            if count > value:
                value = count

    return value


for i in range(case):
    for j in range(case):
        if j + 1 < case:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            cnt = check(arr)
            answer = max(answer, cnt)
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        if i + 1 < case:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            cnt = check(arr)
            answer = max(answer, cnt)
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(answer)


# 조건 개선

case = int(input())
arr = [list(input()) for _ in range(case)]
answer = 0


def check(arr):
    value = 1
    for i in range(case):
        count = 1
        for j in range(1, case):
            if arr[i][j] == arr[i][j - 1]:
                count += 1
            else:
                count = 1

            if count > value:
                value = count

        count = 1
        for j in range(1, case):
            if arr[j][i] == arr[j - 1][i]:
                count += 1
            else:
                count = 1

            if count > value:
                value = count

    return value


for i in range(case):
    for j in range(case):
        if j + 1 < case:
            if arr[i][j] != arr[i][j + 1]:
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
                cnt = check(arr)
                answer = max(answer, cnt)
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        if i + 1 < case:
            if arr[i][j] != arr[i+1][j]:
                arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
                cnt = check(arr)
                answer = max(answer, cnt)
                arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(answer)
