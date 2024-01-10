def solution(i, j, k):
    answer = 0
    for n in range(i,j+1):
        answer += str(n).count(str(k))
    return answer

    # 프로그래머스 연습문제 k의 개수


