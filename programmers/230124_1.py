def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for index, num in enumerate(nums):
        numbers = numbers.replace(num, str(index))
    return int(numbers)

    # 프로그래머스 연습문제 영어가 싫어요