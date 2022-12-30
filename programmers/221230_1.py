def solution(arr):
    arr.sort()
    i = arr[-1]
    count = 0
    while True:
        for k in arr:
            if i%k == 0:
                count += 1
        if count == len(arr):
            return i
        else :
            count = 0
            i += 1

            # 프로그래머스 n개의 최소 공배수

def solution(arr):
    q = sorted(arr, reverse=True)
    answer = q.pop()
    while q:
        temp = q.pop()
        a = min(answer, temp)
        b = max(answer, temp)
        x, y = a, b
        while y:
            x, y = y, x%y
            answer = (a*b)//x
    return answer
    # 유클리드 호제법