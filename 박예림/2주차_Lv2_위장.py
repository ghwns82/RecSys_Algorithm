# https://school.programmers.co.kr/learn/courses/30/lessons/42578
from itertools import combinations
def solution(clothes):
    c_dict = {}
    for c, t in clothes:
        if t not in c_dict:
            c_dict[t] = [c]
        else:
            c_dict[t].append(c)
        
    answer = 1
    for k in c_dict:
        answer *= len(c_dict[k]) + 1 # None인 경우를 고려해 1 더함
        
    answer -= 1 # 조합이 모두 None인 경우(None, None, ...)를 제외
    
    return answer
