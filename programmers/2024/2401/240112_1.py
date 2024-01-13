# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 숫자의 표현

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        sum = 0
        for j in range(i, n + 1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
    return answer


q = solution(15)
assert q == 4
print(q)
