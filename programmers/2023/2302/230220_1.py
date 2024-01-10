def solution(absolutes, signs):
    answer = 0
    for i, k in zip(absolutes, signs):
        if k:
            answer += i
        else:
            answer -= i
    return answer

    # 프로그래머스 연습문제 음양 더하기
