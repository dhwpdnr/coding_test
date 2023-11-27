# 프로그래머스
# 코딩테스트 연습 > 해시 > 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    for comp in completion:
        sumHash -= hash(comp)

    return hashDict[sumHash]


q = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
assert q == "leo"
print(q)

q = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
assert q == "vinko"
print(q)

q = solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
assert q == "mislav"
print(q)
