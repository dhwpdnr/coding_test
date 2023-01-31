def solution(dartResult):
    k = ''
    score = []
    for i in dartResult:
        if i.isnumeric():
            k += i
        elif i == "S":
            k = int(k) ** 1
            score.append(k)
            k = ''
        elif i == "D":
            k = int(k) ** 2
            score.append(k)
            k = ''
        elif i == "T":
            k = int(k) ** 3
            score.append(k)
            k = ''
        elif i == "*":
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == "#":
            score[-1] = score[-1] * -1
    return sum(score)

    # 프로그래머스 2018 카카오 블라인드 채용 [1차] 다트게임
