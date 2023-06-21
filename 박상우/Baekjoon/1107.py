import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
broken = list(map(str, sys.stdin.readline().split()))
cnt = abs(100 - n)

for i in range(1000001):

    for j in str(i):
        if j in broken:
            break

    else:
        cnt = min(cnt, len(str(i)) + abs(i - n))

print(cnt)