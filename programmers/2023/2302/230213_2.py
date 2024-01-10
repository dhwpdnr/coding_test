def solution(n):
    answer = []
    while n != 0 :
        answer.append(n%10)
        n=n//10
    return answer

    # 프로그래머스 연습문제 자연수 뒤집어 배열로 만들기