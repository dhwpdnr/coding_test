def solution(s):
    answer = 0
    i = 0
    arr = list(s)
    while i < len(arr):
        check = []
        for k in arr :
            if len(check) == 0 :
                check.append(k)
            else :
                if k == "]" and check[-1] == "[":
                    check.pop()
                elif k == "}" and check[-1] == "{":
                    check.pop()
                elif k == ")" and check[-1] == "(":
                    check.pop()
                else :
                    check.append(k)
        if len(check) == 0 :
            answer +=1
        i+=1
        a = arr.pop(0)
        arr.append(a)
    return answer

    # 프로그래머스 괄호 회전하기
