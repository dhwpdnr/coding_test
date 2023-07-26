def solution(myString, pat):
    count = 0
    len_pat = len(pat)
    len_myString = len(myString)
    for i in range(len_myString - len_pat + 1):
        if myString[i:i + len_pat] == pat:
            count += 1

    return count
