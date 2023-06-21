# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque

def solution(priorities, location):
    answer = 0
    p_deq = deque(priorities)
    idx_deq = deque(range(len(p_deq))) # 원래 인덱스
    while len(p_deq) > 0: 
        first = p_deq.popleft()
        idx = idx_deq.popleft()

        if len(p_deq) == 0: # p_deq에 값이 하나이면 바로 인쇄
            answer += 1
            return answer

        if first >= max(p_deq): # first가 뒤 원소들의 최댓값보다 같거나 크면 인쇄
            answer += 1 # 인쇄 순서
            if idx == location: # first가 타겟 위치와 같으면 return
                return answer
        else:
            p_deq.append(first) # 목록 맨 뒤로 이동 
            idx_deq.append(idx) # 타깃 원소 이동에 따라 변경
