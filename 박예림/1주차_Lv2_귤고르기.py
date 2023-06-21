# https://school.programmers.co.kr/learn/courses/30/lessons/138476
def solution(k, tangerine):
    answer = 0
    size_cnt = {} # 귤 크기별 개수
    for t in tangerine:
        if t in size_cnt.keys():
            size_cnt[t] += 1
        else:
            size_cnt[t] = 1

    cum_cnt = 0 # 귤 누적 개수
    for cnt in sorted(size_cnt.values(), reverse=True):
        cum_cnt += cnt
        answer += 1
        if cum_cnt >= k:
            return answer
    
    return answer
