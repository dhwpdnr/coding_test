# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 그림 확대
# https://school.programmers.co.kr/learn/courses/30/lessons/181836

def solution(picture, k):
    answer = []

    for row in picture:
        resized = ''

        for pixel in row:
            resized += pixel * k

        for _ in range(k):
            answer.append(resized)

    return answer


q = solution([".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."], 2)
assert q == ["..xxxx......xxxx..", "..xxxx......xxxx..", "xx....xx..xx....xx", "xx....xx..xx....xx",
             "xx......xx......xx", "xx......xx......xx", "..xx..........xx..", "..xx..........xx..",
             "....xx......xx....", "....xx......xx....", "......xx..xx......", "......xx..xx......",
             "........xx........", "........xx........"]
print(q)

q = solution(["x.x", ".x.", "x.x"], 3)
assert q == ["xxx...xxx", "xxx...xxx", "xxx...xxx", "...xxx...", "...xxx...", "...xxx...", "xxx...xxx", "xxx...xxx",
             "xxx...xxx"]
print(q)
