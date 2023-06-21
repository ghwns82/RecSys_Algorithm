# 백준 1389번: 케빈 베이컨의 6단계 법칙 (Silver 1)
# https://www.acmicpc.net/problem/1389
# REF : https://fre2-dom.tistory.com/156

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
friend_arr = [[0 for j in range(n)] for i in range(n)]

# bfs 탐색
def bfs(v, visited):
    queue = deque([v])
    visited[v] = 1

    while queue:
        target = queue.popleft()

        for i in graph[target]:
            if not visited[i]: # 탐색하지 않은 친구이면
                visited[i] = visited[target] + 1
                queue.append(i)

    return visited

# 2차원 그래프
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# 케빈 베이컨 수를 담는 리스트
res = []

# 반복문을 통해 모든 친구 탐색
for i in range(1, n + 1): # 한 사람
    visited = [0] * (n + 1)
    visited = bfs(i, visited)
    res.append(sum(visited))

# 가장 작은 케빈 베이컨의 수를 가지고 있는 사람의 인덱스 + 1 을 해주어 출력
print(res.index(min(res)) + 1)
