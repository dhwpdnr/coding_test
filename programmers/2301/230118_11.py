def solution(s):
    answer = 0
    arr = s.split(" ")
    arr_len = len(arr)
    i = 0
    while i < arr_len :
        if arr[i] == 'Z':
            answer -= int(arr[i-1])
        else :
            answer += int(arr[i])
        i+=1
    return answer

    # 프로그래머스 컨트롤 제트