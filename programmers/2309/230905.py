# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 달리기 경주
# https://school.programmers.co.kr/learn/courses/30/lessons/178871?language=python3

def solution(players, callings):
    result = {player: index for index, player in enumerate(players)}
    for who in callings:
        idx = result[who]
        result[who] -= 1
        result[players[idx - 1]] += 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    return players


q = solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])
assert q == ["mumu", "kai", "mine", "soe", "poe"]
print(q)
