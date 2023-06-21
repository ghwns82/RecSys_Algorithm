# https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque

def solution(bridge_length, weight, truck_weights):
    t = 0 # 경과 시간 (초)
    truck_w = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    while bridge:
        t += 1
        bridge.popleft()
        
        if truck_w:
            if sum(bridge) + truck_w[0] <= weight: # 가장 앞에 대기하고 있는 트럭이 와도 제한 무게를 넘지 않으면
                bridge.append(truck_w.popleft()) # 다리에 추가
            else:
                bridge.append(0) # 길이 재기 위함
    
    return t
