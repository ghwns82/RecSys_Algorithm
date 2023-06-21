# https://school.programmers.co.kr/learn/courses/30/lessons/42586
import math

def solution(progresses, speeds):
    answer = []
    days = []
    
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))
    
    md = days[0] 
    start = 0
    for i in range(len(days)):
        if days[i] > md:
            md = days[i]
            answer.append(len(days[start : i])) # 뒤 원소가 앞 원소보다 작거나 같으면 같이 배포

            start = i
            
    if len(speeds)-sum(answer) != 0:
        answer.append(len(speeds)-sum(answer))
        
    return answer
