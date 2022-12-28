def solution(n):
    i = 1
    answer = []
    while i <= n:
        if i%2 == 1:
            answer.append(i)
        i += 1
    return answer

    # 프로그래머스 코딩테스트 입문