def solution(n, s):
    if n > s: return [-1]
    
    div = s // n
    mod = s % n
    answer = [div] * n
    for i in range(mod):
        answer[i] += 1
    answer.sort()
    return answer