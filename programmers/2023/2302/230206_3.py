def solution(score):
    avg = []
    answer = []
    for i in score:
        avg.append(sum(i) / 2)
    sorted_avg = sorted(avg, reverse=True)
    for i in avg:
        answer.append(sorted_avg.index(i) + 1)
    return answer

    # 프로그래머스 연습문제 등수 메기기
