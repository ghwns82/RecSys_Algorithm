# idea
----
1. 동명이인이 존재    
2. set를 이용해 차집합으로는 해결 x
3. defaultdict으로 3번 돌리면 됨

# solution
----
```
from collections import defaultdict
def solution(participant, completion):
    dic = defaultdict(int)
    for p in participant: dic[p] += 1
    for p in completion: dic[p] -= 1
    for p in dic: 
        if dic[p] != 0: return p
```
