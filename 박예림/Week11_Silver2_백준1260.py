# 백준 1260번: DFS와 BFS (Silver 2)
# https://www.acmicpc.net/problem/1260
# REF: https://ji-gwang.tistory.com/291

from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().rstrip().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = True
    graph[b][a] = True

visited_dfs = [False] * (N + 1) # dfs의 방문 기록
visited_bfs = [False] * (N + 1) # bfs의 방문 기록

# 보통 BFS는 queue로 구현
def bfs(V):
    q = deque([V])
    visited_bfs[V] = True
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N + 1):
            if not visited_bfs[i] and graph[V][i]: # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
                q.append(i)
                visited_bfs[i] = True # 방문 처리

# 보통 DFS는 재귀로 구현
def dfs(V):
    visited_dfs[V] = True # 방문 처리
    print(V, end=" ")
    for i in range(1, N + 1):
        if not visited_dfs[i] and graph[V][i]: # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i) # i값으로 더 깊이 탐색

dfs(V)
print()
bfs(V)
