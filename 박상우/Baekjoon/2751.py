import sys

n = int(input())
srt = []
for _ in range(n):
    srt.append(int(sys.stdin.readline()))
    
srt.sort()
for i in srt:
    print(i)