# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 바탕화면 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    a, b = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]


q = solution([".#...", "..#..", "...#."])
assert q == [0, 1, 3, 4]
print(q)

q = solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])
assert q == [1, 3, 5, 8]
print(q)

q = solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."])
assert q == [0, 0, 7, 9]
print(q)

q = solution(["..", "#."])
assert q == [1, 0, 2, 1]
print(q)
