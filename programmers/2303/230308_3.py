def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    lottos = [i for i in lottos if i != 0]
    result = 0
    for num in lottos:
        if num in win_nums:
            result += 1
    return [rank[result + (6 - len(lottos))], rank[result]]

    # 프로그래머스 연습문제 로또의 최고 순위와 최저 순위
