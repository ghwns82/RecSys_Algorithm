# https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    answer = False
    ans = []
    for i in s:
        if i == '(':
            ans.append(0)
        elif len(ans) != 0:
            ans.pop()
        else: # ans에 아무것도 없는데 ")"가 나오는 경우. 즉 "("가 나오지 않고 ")"가 나오는 경우
            return False
    
    if len(ans) == 0:
        answer = True
        
    return answer
