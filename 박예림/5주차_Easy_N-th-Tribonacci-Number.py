# [LeetCode] 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        elif n in {1, 2}: return 1
        else:
            t = [0, 1, 1] # T_(n+3) 계산을 위한 T_n, T_(n+1), T_(n+2) 저장
            for i in range(3, n):
                tmp = sum(t)
                t[0] = t[1]
                t[1] = t[2]
                t[2] = tmp
            return sum(t)
