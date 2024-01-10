from collections import Counter


def solution(k, tangerine):
    count = Counter(tangerine)
    sorted_count = count.most_common()
    answer = 0
    for i in sorted_count:
        k -= i[1]
        answer += 1
        if k <= 0:
            break
    return answer

    # 프로그래머스 연습문제 귤 고르기
