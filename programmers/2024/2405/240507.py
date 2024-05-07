# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/250126
# 코딩테스트 연습 > 코딩 기초 트레이닝 > [PCCE 기출문제] 8번 / 창고 정리

def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            clean_num.append(num[i])

    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer


q = solution(["pencil", "pencil", "pencil", "book"], [2, 4, 3, 1])
assert q == "pencil"
print(q)

q = solution(["doll", "doll", "doll", "doll"], [1, 1, 1, 1])
assert q == "doll"
print(q)

q = solution(["apple", "steel", "leaf", "apple", "leaf"], [5, 3, 5, 3, 7])
assert q == "leaf"
print(q)

q = solution(["mirror", "net", "mirror", "net", "bottle"], [4, 1, 4, 1, 5])
assert q == "mirror"
print(q)
