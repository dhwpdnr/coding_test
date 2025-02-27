# 프로그래머스
# 코딩테스트 연습 > 2020 카카오 인턴십 > 키패드 누르기
# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def dist(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)


def solution(numbers, hand):
    keypad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        "*": [3, 0], 0: [3, 1], "#": [3, 2]
    }
    answer = ''
    left_finger = keypad["*"]
    right_finger = keypad["#"]
    for number in numbers:
        if number in [1, 4, 7]:
            left_finger = keypad[number]
            answer += "L"
        elif number in [3, 6, 9]:
            right_finger = keypad[number]
            answer += "R"
        else:
            left_dist = dist(left_finger, keypad[number])
            right_dist = dist(right_finger, keypad[number])
            if left_dist > right_dist:
                right_finger = keypad[number]
                answer += "R"
            elif left_dist < right_dist:
                left_finger = keypad[number]
                answer += "L"
            else:
                if hand == "right":
                    right_finger = keypad[number]
                    answer += "R"
                else:
                    left_finger = keypad[number]
                    answer += "L"

    return answer


q = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
assert q == "LRLLLRLLRRL"
print(q)

q = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
assert q == "LRLLRRLLLRR"
print(q)

q = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
assert q == "LLRLLRLLRL"
print(q)
