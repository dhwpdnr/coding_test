from collections import Counter


def solution(X, Y):
    answer = '-1'

    list_X, list_Y = list(X), list(Y)
    set_X, set_Y = set(list_X), set(list_Y)
    # 개수 확인을 위해 Counter 사용
    cnt_X, cnt_Y = Counter(list_X), Counter(list_Y)

    # 교집합 확인
    intersection = set_X & set_Y

    # 교집합 있으면
    if intersection:
        answer = ''
        sorted_number = sorted(intersection, reverse=True)

        for num in sorted_number:
            # 교집합 원소의 개수 중 X나 Y에 더 적게 나온 수만큼 answer 에 추가
            answer += num * min(cnt_X[num], cnt_Y[num])

        # 전체 리스트의 합이 0이면 "0" 리턴
        if sum(list(map(int, list(answer)))) == 0:
            answer = "0"

    return answer

    # 프로그래머스 연습문제 숫자 짝궁
