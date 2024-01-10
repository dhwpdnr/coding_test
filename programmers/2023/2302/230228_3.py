def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        num = bin(a1 | a2)
        num = num[2:].zfill(n)
        answer.append(num.replace("1", "#").replace("0", " "))
    return answer

    # 프로그래머스 연습문제 [1차] 비밀지도