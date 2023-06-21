import sys
sys.setrecursionlimit(10000)

t = int(input())

def dfs(x,y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if farm[ny][nx] == 1:
                farm[ny][nx] = 0
                dfs(nx, ny)        


for _ in range(t):
    cnt = 0
    m,n,k = map(int,input().split())
    farm = [[0]*m for _ in range(n)]

    for __ in range(k):
        x, y = map(int,input().split())
        farm[y][x] = 1 
    
    for x in range(m):
        for y in range(n):
            if farm[y][x] == 1:
                farm[y][x] = 0
                dfs(x,y)
                cnt += 1
    print(cnt)
    
        