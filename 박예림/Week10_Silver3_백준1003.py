# 백준 1003번: 피보나치 함수 (Silver 3)
# https://www.acmicpc.net/problem/1003
# Ref: https://bio-info.tistory.com/122

T = int(input())
N = [int(input()) for _ in range(T)]

for n in N:
    zero_cnt, one_cnt = 1, 0 # 둘이 같은 피보나치 수열에 있음
    for i in range(n):
        zero_cnt, one_cnt = one_cnt, zero_cnt + one_cnt
    print(zero_cnt, one_cnt)
