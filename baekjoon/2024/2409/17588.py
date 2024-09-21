def missing_numbers(number_list):
    max_number = max(number_list)

    range_number_list = set(range(1, max_number + 1))

    missing_number_list = range_number_list - set(number_list)

    return sorted(missing_number_list)


def print_answer(answer):
    if answer:
        for ans in answer:
            print(ans)
    else:
        print("good job")


number_list = []

for _ in range(int(input())):
    number = int(input())
    number_list.append(number)

print_answer(answer=missing_numbers(number_list=number_list))
