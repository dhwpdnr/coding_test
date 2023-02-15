def solution(x):
    n_list = list(map(int, str(x)))
    sum_all = sum(n_list)
    if x % sum_all == 0:
        return True
    else:
        return False

    # 프로그래머스 연습문제 하샤드 수


def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

    # 리스트 컴프리 헨션 사용과 if 문 생략에 따른 간단해진 코드