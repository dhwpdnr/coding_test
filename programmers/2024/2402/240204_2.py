# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/250121
# 코딩테스트 연습 > PCCE 기출문제 > [PCCE 기출문제] 10번 / 데이터 분석

def solution(data, ext, val_ext, sort_by):
    answer = []
    dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    for d in data:
        value = d[dict[ext]]
        if value <= val_ext:
            answer.append(d)
    answer.sort(key=lambda x: x[dict[sort_by]])
    return answer


# 리스트 컴프리헨션 사용 코드
def solution(data, ext, val_ext, sort_by):
    dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    answer = [d for d in data if d[dict[ext]] < val_ext]
    return sorted(answer, key=lambda x: x[dict[sort_by]])


q = solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain")
assert q == [[3, 20300401, 10, 8], [1, 20300104, 100, 80]]
print(q)
