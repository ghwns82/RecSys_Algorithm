# idea
---
1. 장르별 총 플레이횟수가 필요 -> 정렬
2. 장르에 속한 노래들이 필요 -> 저장
3. 장르를 플레이횟수에 따라 정렬하고
4. 그 순서대로 장르에 속한 곡들을 다시 플레이 횟수에 따라 정렬

# solution
---
```
from collections import defaultdict
def solution(genres, plays):
    answer = []
    g_dic = defaultdict(list)
    g_count = defaultdict(int)
    for i, g in enumerate(genres): 
        g_count[g] += plays[i]
        g_dic[g].append((i, plays[i]))
    to_sort = []
    for g in g_count: to_sort.append((g, g_count[g]))
    to_sort.sort(key = lambda x: x[1], reverse = True)
    
    for g, count in to_sort:
        g_dic[g].sort(key = lambda x: x[1], reverse = True)
        if len(g_dic[g]) > 2: g_dic[g] = g_dic[g][:2]
        for gen, count in g_dic[g]:
            answer.append(gen)
    return answer
```
