def solution(n):
    answer = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            answer.append(i)
            if (i ** 2) != n:
                answer.append(n // i)
    answer.sort()
    return answer

    # 프로그래머스 연습문제 약수 구하기
