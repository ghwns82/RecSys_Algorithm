# 백준 1181번: 단어 정렬 (https://www.acmicpc.net/problem/1181)
from collections import defaultdict
n = int(input())
words = [input() for _ in range(n)]
words = list(set(words)) # 중복 제거

size_cnt = defaultdict(list)
for w in words:
  size_cnt[len(w)].append(w)

answer = []
for item in sorted(size_cnt.items()): # size 값 기준으로 오름차순으로 정렬
  answer += sorted(item[1]) # 단어 오름차순 정렬

for a in answer:
  print(a)
