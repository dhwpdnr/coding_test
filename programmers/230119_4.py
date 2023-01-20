from collections import Counter
def solution(str1, str2):
    s1 = str1.lower()
    s2 = str2.lower()
    s1_len = len(s1)
    s2_len = len(s2)
    arr1 = []
    arr2 = []
    i = 0
    n = 0
    while i < s1_len - 1 :
        if ord(s1[i]) < 97 or ord(s1[i]) > 122 :
            pass
        elif ord(s1[i+1]) < 97 or ord(s1[i+1]) > 122 :
            pass
        else :
            arr1.append(s1[i]+s1[i+1])
        i += 1
    while n < s2_len - 1 :
        if ord(s2[n]) < 97 or ord(s2[n]) > 122 :
            pass
        elif ord(s2[n+1]) < 97 or ord(s2[n+1]) > 122 :
            pass
        else :
            arr2.append(s2[n]+s2[n+1])
        n += 1
    if len(arr1) == 0 and len(arr2) == 0 :
        return 65536
    dict1 = Counter(arr1)
    dict2 = Counter(arr2)
    inter = list((dict1 & dict2).elements())
    union = list((dict1 | dict2).elements())
    answer = int(len(inter) / len(union) * 65536)
    return answer

    # 프로그래머스 2018 카카오 [1차] 뉴스 클러스터링
