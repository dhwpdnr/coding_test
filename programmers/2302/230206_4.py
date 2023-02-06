def solution(babbling):
    answer = 0
    for i in babbling:
        word = i.replace("aya", " ")
        word = word.replace("woo", " ")
        word = word.replace("ye", " ")
        word = word.replace("ma", " ")
        if word.strip() == "":
            answer += 1
    return answer

   # 프로그래머스 연습문제 옹알이(1)