def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

    # 프로그래머스 연습문제 머쓱이보다 키 큰 사람


def another(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

    # 배열의 인덱스로 접근한 문제
