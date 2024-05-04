# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/250128
# 코딩테스트 연습 > 코딩 기초 트레이닝 > [PCCE 기출문제] 6번 / 가채점


def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i] - 1]:
            answer.append("Same")
        else:
            answer.append("Different")

    return answer


q = solution([1], [100], [100, 80, 90, 84, 20])
assert q == ["Same"]
print(q)

q = solution([3, 4], [85, 93], [85, 92, 38, 93, 48, 85, 92, 56])
assert q == ["Different", "Same"]
print(q)
