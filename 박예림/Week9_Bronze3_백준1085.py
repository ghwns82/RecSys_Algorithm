# 백준 1085번: 직사각형에서 탈출 (https://www.acmicpc.net/problem/1085)

x, y, w, h = map(int, input().split())
print(min(w-x, h-y, x, y))
