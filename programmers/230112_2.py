def solution(n):
    answer = 0
    i = 1
    while i <= n :
        k = 1
        count = 0
        while k <= i:
            if i % k == 0:
                count += 1
            k += 1
        if count >= 3 :
            answer += 1
        i += 1
    return answer

    # 합성수 찾기