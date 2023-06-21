n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n+1):
    graph[i].sort()
    
visited = [False]*(n+1)
dfs_list = []
bfs_list = []

def dfs(v):
    visited[v] = True
    dfs_list.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(v)

from collections import deque

visited = [False]*(n+1)
queue = deque()
queue.append(v)

while queue:
    k = queue.popleft()
    if visited[k] == True:
        pass
    else:
        visited[k] = True 
        bfs_list.append(k)
        for i in graph[k]:
            queue.append(i)

print(" ".join(map(str,dfs_list)))
print(" ".join(map(str,bfs_list)))