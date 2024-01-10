def solution(s):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer = ""
    word = ""
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            word += s[i]
            if word in num_list:
                answer += str(num_list.index(word))
                word = ""
    return int(answer)

    # 프로그래머스 연습문제 숫자 문자열과 영단어
