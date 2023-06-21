def solution(prices):
    answer = [0] * len(prices)
    
    # 자기 자신보다 작은 수가 나오는 순간(위치)을 찾아야 함
    # 해당 위치의 인덱스 - 자기 자신의 인덱스 = 가격이 떨어지지 않은 기간 (초)
    # 다만, 자기 자신보다 작은 수가 나오는 순간이 없었다면 끝까지 가격이 떨어지지 않은 것이므로 최대 길이 계산
    
    # 자기 자신 (고정 인덱스) = i, 계속 움직이는 인덱스 = j
    for i in range(len(prices)):
        flag = False
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]: # 자기 자신보다 작은 수가 나왔을 때
                answer[i] = j - i # 가격이 떨어지지 않은 기간 계산
                flag = True
                break
        if not flag: # 자기 자신보다 작은 수가 끝까지 안나왔을 때
            answer[i] = len(prices) - (i+1) # 최대 길이
            
    return answer
