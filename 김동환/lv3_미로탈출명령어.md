# Idea
----
1. 단순한 BFS라 생각했지만 시간 초과로 실패 -> 막힌 곳이 없어서 k 4^k 시간 복잡도
2. Greedy로 선회
3. 출발지 -> 목적지까지 필요한 필수적인 커맨드가 있음(ex. up up left left)
4. 그럼 k를 채우기 위해서는 잉여 커맨드가 필요하고 이는 k - (최단 거리)를 2로 나눈만큼 가능
5. 필요없는 커맨드를 하면 반대로 한 번 더 해야하기 때문
6. 최대한 d l r u 순으로 움직이고 잉여 커맨드를 할 수 있으면 필수적인 커맨드 외의 동작을 할 수 있음
7. 커맨드 별로 남은 횟수를 저장 -> 필수적인 커맨드가 있으므로 초기에는 d : 0 l : 2 r : 0 u : 2
8. 잉여 커맨드 o -> 가능한 방향으로 남은 개수에 상관없이 d l r u 우선순위로 이동 & 반대 커맨드 + 1
9. 잉여 커맨드 x -> 가능한 방향 중 남은 개수가 0 이상인 것으로 이동 & 커맨드 - 1

# Code
----
```
def solution(n, m, x, y, r, c, k):
    
    ### 목적지에 가려면 최소한의 횡이동과 종이동의 거리가 정해져있음
    
    ##최대한 d l r u 순으로 접근
    ##현재 위치 -> 목적지 최단 거리 =  uu ll
    ##만약 필요 없는 것 d r 추가 되면 cost + 2가 됨
    
    ##잉여 거리 = (k - 최단 거리) / 2
    ##잉여 거리/2 만큼 다른 방향으로 움직일 수 있음
    ##움직여얄 커맨드 목록 생성 -> 2 : 2, 4 : 2
    ##잉여 거리가 남아있다면 -> dlru 순으로 움직일 수 있는 방향으로 움직임
    ##잉여 거리 - 1 해주고 cancel 할 것 넣어줌  2:2, 4:2, 3:1
    ##잉여 거리가 남으면 반복
    ##잉여 거리 없으면 이동가능한 방향 중 가장 작은 것 순서대로 움직이기
    dist = abs(x-r)+abs(y-c)
    left = (k -dist) /2
    
    if k-dist < 0 or (k-dist)%2 != 0: return "impossible"
    
    mapper = {'1':'d','2':'l','3':'r','4':'u'}

    left_commands = {i:0 for i in range(1, 5)}
    cm_mapper = {1:(1,0),2:(0,-1),3:(0,1),4:(-1,0)}
    opp_mapper = {1:4, 2:3, 3:2, 4:1}
    
    vertical = r-x
    if vertical > 0: left_commands[1] = abs(vertical)
    else:left_commands[4] = abs(vertical)
    
    horizontal = c-y
    if horizontal > 0: left_commands[3] = abs(horizontal)
    else:left_commands[2] = abs(horizontal)
    

    c_x = x
    c_y = y
    log = 0
    d = k
    
    while d > 0:   

        for cm in left_commands:
            d_x, d_y = cm_mapper[cm]
            
            if (left_commands[cm] <= 0) & (left >= 1):
                if (0< c_x+d_x <= n) & (0<c_y + d_y<= m):
                    log += cm
                    left_commands[opp_mapper[cm]] += 1
                    left -= 1
                    c_x += d_x
                    c_y += d_y
                    break
                    
            elif left_commands[cm] > 0:
                if (0< c_x+d_x <= n) & (0<c_y + d_y<= m):
                    left_commands[cm] -= 1
                    log += cm
                    c_x += d_x
                    c_y += d_y
                    break
                    
        d -= 1
        if d > 0: log *= 10
        

    log = str(log)

    return ''.join([mapper[s] for s in log])
        
    
