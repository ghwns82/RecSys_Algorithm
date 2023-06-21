# [LeetCode] 1025. Divisor Game
# https://leetcode.com/problems/divisor-game/
class Solution:
    def divisorGame(self, n: int) -> bool:
        if n % 2 == 0: # 둘 다 최적으로 움직이기 때문에, 짝수이면 Alice가 이기고 홀수이면 Bob이 이기는 규칙 존재
            return True
        else:
            return False
