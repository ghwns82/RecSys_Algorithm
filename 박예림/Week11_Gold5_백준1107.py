# 백준 1107번: 리모컨 (Gold 5)
# https://www.acmicpc.net/problem/1107
# REF: https://fre2-dom.tistory.com/477

import sys
input = sys.stdin.readline

n = int(input()) # 찾고자 하는 채널
m = int(input()) # 고장난 버튼 개수
broken = list(map(str, input().rstrip().split()))

# +, - 만 사용하여 이동하는 경우 (리모컨을 눌러야 하는 최대 개수)
ans = abs(100 - n) # 현재 채널 = 100

# 완전 탐색
for i in range(1000001):
    for j in str(i):
        if j in broken: # 고장난 버튼의 숫자인 경우
            break
    
    else: # 버튼으로 숫자를 입력할 수 있는 경우
        # min(기존 답, 버튼 누른 횟수 + 버튼으로 누른 채널로부터 타겟 채널까지의 차이)
        ans = min(ans, len(str(i)) + abs(i - n))

print(ans)
