# [LeetCode] 55. Jump Game
# https://leetcode.com/problems/jump-game/description/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums) - 1  
        curr_idx = 0
        next_idx = nums[curr_idx]

        if next_idx >= last_idx: return True
        
        while curr_idx < next_idx: # 반복적으로 최대한 큰 step으로 이동하여 last_idx를 도달하거나 넘으면 True
            curr_idx += 1
            next_idx = max(next_idx, curr_idx + nums[curr_idx]) 
            if next_idx >= last_idx: return True
        
        return False

# reference : https://www.jutopia.net/algorithm/lc55/
