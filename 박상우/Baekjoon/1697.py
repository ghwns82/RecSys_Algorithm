n,m = map(int,input().split())

from collections import deque

queue = deque([n])
max_len = 100000
visited = [0] * (max_len + 1)

while queue:
    n = queue.popleft()
    if n==m:
        print(visited[n])
        break
    else:
        for i in (n-1,n+1,n*2):
            if 0 <= i <= max_len and not visited[i]:
                visited[i] = visited[n] + 1 
                queue.append(i)
