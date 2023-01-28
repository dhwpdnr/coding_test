def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer

    # 프로그래머스 연습문제 n의 배수 구하기
