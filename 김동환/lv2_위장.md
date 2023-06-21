# idea
----
1. 단순한 조합
2. 아무것도 안 입은 경우가 있으니 + 1 해줌
3. 다 안 입으면 안되니 마지막에 -1 

# solution
---
```
from collections import defaultdict
from itertools import product
def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for item_cat in clothes: dic[item_cat[1]] += 1
    for key in dic: answer *= dic[key] + 1
    
    return answer - 1

```
