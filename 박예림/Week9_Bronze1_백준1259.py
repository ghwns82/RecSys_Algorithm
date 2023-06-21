# 백준 1259번: 팰린드롬수 (Bronze 1)
# https://www.acmicpc.net/problem/1259

while True:
  n = input()

  if n == '0': 
    break

  mid = len(n) // 2
  if len(n) == 1 or n[:mid] == n[::-1][:mid]:
    print("yes")
  else:
    print("no")
