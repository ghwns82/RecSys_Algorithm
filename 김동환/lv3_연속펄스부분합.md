# Idea
----
1. 길이가 50만 -> n^2은 불가
2. 펄스 수열을 곱함
3. 이 수열의 부분합의 절댓값의 최대 = 최대값
4. DP
5. p_con = ? ~ n-1까지 했을 때 양수 최대
6. n_con ? ~ n-1 까지 했을 때 음수 최소
7. con = p_con & n_con 중 절대값 최대

n일 때 s = con & p_con & n_con & s   
DP는 아직 어렵게 느껴진다. 무작정 규칙을 나열하기보다는 n일 때의 어떤 형식을 갖는지 점화식을 논리적으로 정하는 것이 우선.

# Code
----
```
def solution(sequence):
    import math
    
    pulse1 = [-1 if i%2 == 0 else 1 for i in range(len(sequence))]

    for i in range(len(sequence)): pulse1[i] = sequence[i]*pulse1[i] 
    
    s = -1
    p_con = math.inf * -1
    n_con = math.inf
    con = 0
    
    for n in pulse1:
        
        p_con = max(n, n+p_con)
        n_con = min(n, n+n_con)
        
        v1 = abs(p_con)
        v2 = abs(n_con)
        v3 = abs(n)
        v4 = abs(p_con)
        v5 = abs(n_con)
    
        s = max(v1,v2,v3,v4,v5, s)
    

    return s
