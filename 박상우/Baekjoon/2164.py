n = int(input())
from collections import deque

queue = deque()

for i in range(n):
    queue.append(i+1)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])
    