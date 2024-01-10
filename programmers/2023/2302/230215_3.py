def solution(n):
    for i in range(1, n):
        if n % i == 1:
            return i

    # 프로그래머스 연습문제 나머지가 1이 되는 수 찾기
