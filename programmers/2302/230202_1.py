def solution(spell, dic):
    spell = "".join(sorted(spell))
    for i in dic:
        i = "".join(sorted(i))
        if i == spell:
            return 1
    return 2

    # 프로그래머스 연습문제 외계어 사전
