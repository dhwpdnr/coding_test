def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        count = 0
        for k in range(1, i + 1):
            if i % k == 0:
                count += 1
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

   # 프로그래머스 연습문제 약수의 개수와 덧셈