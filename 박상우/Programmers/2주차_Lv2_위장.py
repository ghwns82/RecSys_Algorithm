def solution(clothes):
    from collections import defaultdict, Counter
    answer = 1
    clothes_dicts = {}
    for i in clothes:
        if i[1] not in clothes_dicts:
            clothes_dicts[i[1]] = 1
        else:
            clothes_dicts[i[1]] += 1
    for j in clothes_dicts.values():
        answer *= j+1
    return answer -1