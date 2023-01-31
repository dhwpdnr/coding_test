def solution(s):
    arr = []
    rm = []
    answer = []
    s2 = s[1:-1]
    ls = s2.split("}")
    ls.pop()
    for i in ls:
        if ls.index(i) == 0 :
            i = i[1:]
            i = i.split(",")
            arr.append(i)
        else :
            i = i[2:]
            i = i.split(",")
            arr.append(i)
    arr.sort(key=len)
    for i in arr:
        for k in rm :
            i.remove(k)
        answer.append(i[0])
        rm.append(i[0])
    intarr = list(map(int, answer))
    return intarr

    # 2019 카카오 개발자 겨울 인턴십 튜플