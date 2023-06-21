# 백준 2751번: 수 정렬하기 2 (Silver 5)
# https://www.acmicpc.net/problem/2751

n = int(input())
nums = [int(input()) for _ in range(n)]

for i in sorted(nums): # Python3로 제출 시에는 시간 초과 .. PyPy3로 성공
    print(i)
