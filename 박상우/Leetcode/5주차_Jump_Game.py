class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length ==1:
            return True
        visited = [True] * length 

        schedule = [0]
        visited[0] = False 
        while schedule:
            cur = schedule.pop()
            for i in range(1,nums[cur]+1):
                if cur + i < length and visited[cur+i]:
                    visited[cur+i] = False
                    if (cur+i) == length -1:
                        return True
                    schedule.append(cur+i)
        return False