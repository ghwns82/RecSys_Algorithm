# Idea
1. 노드와 연결된 정보를 저장한다
2. 적은 수 대로 정렬한다

DFS
1. q를 pop해서 start node를 방문하고 마킹한다.
2. 연결된 노드 중 방문하지 않았고, 가장 적은 수의 노드를 찾는다
3. 갈 수 있는 노드를 찾으면 q에 넣고 그 노드를 방문한다.
4. 더 이상 방문할 노드가 없으면 종료한다.

BFS
1. q를 pop해서 start node를 방문하고 마킹한다.
2. 연결된 노드 중 방문하지 않았고, 가장 적은 수의 노드를 찾는다
3. 갈 수 있는 노드를 모두 q에 넣는다.
4. 더 이상 방문할 노드가 없으면 종료한다.

근데 왜 틀린지 모르겠다. 아시는 분은 댓글 좀...

# Code
```
import sys
from collections import defaultdict, deque
import copy

n, m,  v = map(int,input().split())

edge = defaultdict(list)
for _ in range(m):
    start, end = map(int,input().split())
    edge[start].append(end)
    edge[end].append(start)
    
for n in edge: edge[n].sort()
    
def dfs(v, edge, done, result): 
    done.add(v)
    print(v, end=' ')
    if edge[v]:
        for next_v in edge[v]: 
            if next_v not in done:
                result = dfs(next_v , edge, done, result)
    
def bfs(v, edge):
    done = set()
    q = deque()
    q.append(v)
    while q:
        node = q.popleft()
        done.add(node)
        print(node,end=' ')
        for n in edge[node]:
            if n not in done: 
                q.append(n)
                done.add(n)
    
if v > n: 
    print('')
    print('')
else:
    done = set()
    dfs(v, copy.deepcopy(edge), done, '')
    print()
    bfs(v, copy.deepcopy(edge))
```
