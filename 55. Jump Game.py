class Solution:
    def canJump(self, nums: List[int]) -> bool:
        Max = 0
        for i in range(len(nums)):
            if i > Max:
                return False
            Max = max(Max, i + nums[i])
        return True
