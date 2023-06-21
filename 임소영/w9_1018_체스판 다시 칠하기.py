n,m = map(int, input().split())
chess = list()

for i in range(0, n):
    chess.append(input())

cnt = [0 for i in range((n-7) * (m-7))]
ex = ['WBWBWBWBBWBWBWBW', 'BWBWBWBWWBWBWBWB']
w = -1
flag = 0
num = 0
c1 = 0
c2 = 0

for k in range(0, n-7):
    for t in range(0, m-7):
        for i in range(k, 8+k):
            for j in range(t, 8+t):
                w = w+1
                if chess[i][j] == ex[0][w]:
                    c1 = c1 + 0
                else:
                    c1 = c1 + 1
                    
                if chess[i][j] == ex[1][w]:
                    c2 = c2 + 0
                else:
                    c2 = c2 + 1

            if (k-i) % 2 == 1 : w = -1
        cnt[num] = min(c1, c2)
        num = num + 1
        c1 = 0
        c2 = 0
        
print(min(cnt))
