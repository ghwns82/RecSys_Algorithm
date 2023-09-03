# Idea
----
1. 온도는 유지하거나 내리거나 올리거나
2. 그럼 지금의 온도는 전 타임에서 내리거나 올리거나 유지한 온도
3. 마찬가지로 다음 타임의 온도는 지금 온도에서 내리거나 올리거나 유지한 온ㄷ
4. DP 방식으로 접근
5. 현재 타임이 t라고 하면 이전 타임에서 가능했던 온도와 그에 해당하는 코스트가 있을 것이라 가정
6. t-1 (26 10), (25 12), (27 11)
7. 그러면 내가 다음 타임으로 할 수 있는 온도는 26, 25, 27에서 올리거나 내리거나 유지
8. 그리고 타음 타임에 사람이 있거나 없거나에 따라서 설정할 수 있는 온도가 다름
9. 이를 DP로 계산


# Code
----
```
from collections import defaultdict
import math
def solution(temperature, t1, t2, a, b, onboard):
    
    out_t = temperature
    answer = 0

    dp = [defaultdict(lambda: float('inf')) for _ in range(len(onboard))]
 
    dp[0][out_t] = 0
    
    for i in range(len(onboard)-1):
        next_p = onboard[i+1]
       
        for tmp_t in dp[i]:
            past_cost = dp[i][tmp_t]
            
            ###온도 유지하는 경우
            if (next_p == 1) & (t1 <= tmp_t) & (tmp_t <= t2):
                if tmp_t == out_t: ##실외 온도 = 실내 온도
                    dp[i+1][tmp_t] = min(dp[i+1][tmp_t], past_cost)
                elif tmp_t != out_t: ##실외 온도 != 실내 온도
                    dp[i+1][tmp_t] = min(dp[i+1][tmp_t], past_cost+b)
            elif next_p == 0:
                if tmp_t == out_t: ##실외 온도 = 실내 온도
                    dp[i+1][tmp_t] = min(dp[i+1][tmp_t], past_cost)
                elif tmp_t != out_t: ##실외 온도 != 실내 온도
                    dp[i+1][tmp_t] = min(dp[i+1][tmp_t], past_cost+b)

            ### 온도 올리기
            #####사람 있는 경우
            if (next_p == 1) & (tmp_t+1 <= t2) & (tmp_t+1 >= t1):
                if tmp_t < out_t:  ####가만히 나두면 올라감, off
                    dp[i+1][tmp_t+1] = min(dp[i+1][tmp_t+1], past_cost)
                else:  
                    dp[i+1][tmp_t+1] = min(dp[i+1][tmp_t+1], past_cost+a)
            ####사람 없는 경우
            elif next_p == 0: 
                if tmp_t < out_t:  ####가만히 나두면 올라감
                    dp[i+1][tmp_t+1] = min(dp[i+1][tmp_t+1], past_cost)
                else:  
                    dp[i+1][tmp_t+1] = min(dp[i+1][tmp_t+1], past_cost+a)
                
            ### 온도 내리기
            #####사람 있는 경우
            if (next_p == 1) & (tmp_t-1 >= t1) & (tmp_t-1 <= t2):
                if tmp_t > out_t:  ####가만히 나두면 내려감, off
                    dp[i+1][tmp_t-1] = min(dp[i+1][tmp_t-1], past_cost)
                else:  
                    dp[i+1][tmp_t-1] = min(dp[i+1][tmp_t-1], past_cost+a)
            ####사람 없는 경우
            elif next_p == 0: 
                if tmp_t > out_t:  ####가만히 나두면 내려감, off
                    dp[i+1][tmp_t-1] = min(dp[i+1][tmp_t-1], past_cost)
                else: 
                    dp[i+1][tmp_t-1] = min(dp[i+1][tmp_t-1], past_cost+a)
        
    return min(dp[-1].values())
