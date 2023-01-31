def solution(nums):
    answer = 0
    arr = []
    for i in nums:
        if len(arr) >= len(nums) / 2:
            break
        if i in arr:
            pass
        else:
            arr.append(i)

    return len(arr)

    # 포켓몬