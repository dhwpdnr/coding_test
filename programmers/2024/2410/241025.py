def solution(bandage, health, attacks):
    count = 0
    max_health = health
    for i in range(1, attacks[-1][0] + 1):
        if i == attacks[0][0]:
            health -= attacks[0][1]
            attacks.pop(0)
            count = 0
        else:
            health = min(max_health, health + bandage[1])
            count += 1
            if count == bandage[0]:
                health = min(max_health, health + bandage[2])
                count = 0

        if health <= 0:
            return -1

    return health


q = solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])
assert q == 5
print(q)

q = solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])
assert q == -1
print(q)

q = solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])
assert q == -1
print(q)

q = solution([1, 1, 1], 5, [[1, 2], [3, 2]])
assert q == 3
print(q)
