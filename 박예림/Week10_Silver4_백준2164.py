# 백준 2164번: 카드2 (Silver 4)
# https://www.acmicpc.net/problem/2164

from collections import deque

cards = deque([i + 1 for i in range(int(input()))]) # 리스트 사용 시 시간 초과

while len(cards) > 1:
    cards.popleft() # list의 pop()은 시간 복잡도가 O(n)이나, deque의 popleft()는 O(1)이므로 시간 복잡도를 줄일 수 있음
    cards.append(cards.popleft())

print(cards[0])
