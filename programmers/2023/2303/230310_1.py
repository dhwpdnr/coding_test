def solution(number, limit, power):
    attack = []
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i ** (1 / 2) + 1)):
            if i % j == 0:
                count += 1
                if j ** 2 != i:
                    count += 1
        if count > limit:
            attack.append(power)
        else:
            attack.append(count)
    return sum(attack)

    # 프로그래머스 연습문제 기사단원의 무기
    # 약수를 구하는 과정에서 1부터 숫자 끝까지 반복을 돌면 시간초과 남
    # 약수 구하는 과정을 단축하기 위해 제곱근까지만 범위 설정