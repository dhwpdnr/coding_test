def solution(numbers, direction):
    answer = []
    if direction == "right" :
        num = numbers.pop()
        numbers.insert(0, num)
        return numbers
    else :
        num = numbers.pop(0)
        print(numbers)
        numbers.append(num)
        return numbers

    #배열 회전시키기