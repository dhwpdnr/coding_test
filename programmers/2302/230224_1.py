def solution(n, m):
    gcd = [i for i in range(min(n, m), 0, -1) if n % i == 0 and m % i == 0]
    lcm = [i for i in range(max(n, m), (n * m) + 1) if i % n == 0 and i % m == 0]
    return [gcd[0], lcm[0]]

    # 프로그래머스 연습문제 최대공약수와 최소공배수