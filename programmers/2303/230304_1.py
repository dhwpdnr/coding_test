def solution(food):
    answer = ''
    count = 1
    for i in food[1:]:
        answer += str(count) * (i // 2)
        count += 1
    return answer + "0" + answer[::-1]

    # 프로그래머스 연습문제 푸드파이터 대회
