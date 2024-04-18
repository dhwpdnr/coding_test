def solution(today, terms, privacies):
    answer = []
    time_dict = dict()
    year, month, day = int(today[0:4]), int(today[5:7]), int(today[8:])

    for term in terms:
        case = term[0]
        time_dict[case] = int(term[2:])

    for i in range(len(privacies)):
        date, case = privacies[i].split()
        p_year, p_month, p_day = map(int, date.split("."))

        p_month += time_dict[case]

        while p_month > 12:
            p_month -= 12
            p_year += 1

        if p_year > year:
            continue

        elif p_year == year:
            if p_month > month:
                continue

            elif p_month == month:
                if p_day > day:
                    continue

        answer.append(i + 1)
    return answer


q = solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
assert q == [1, 3]
print(q)

q = solution("2020.01.01", ["Z 3", "D 5"],
             ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
assert q == [1, 4, 5]
print(q)
