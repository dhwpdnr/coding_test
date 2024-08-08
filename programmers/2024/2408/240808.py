# 프로그래머스
# 코딩테스트 연습 > 동적계획법(Dynamic Programming) > 정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    dp = triangle

    depth = len(dp)
    for i in range(1, depth):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] += dp[i - 1][j]
            elif j == i:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])

    return max(dp[depth - 1])


q = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
assert q == 30
print(q)
