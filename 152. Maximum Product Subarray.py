class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Max_DP = [0] * len(nums)
        Min_DP = [0] * len(nums)        
        Max_DP[0] = nums[0]
        Min_DP[0] = nums[0]
        for i in range(1, len(nums)):
            Max_DP[i] = max(Max_DP[i - 1] * nums[i], nums[i], Min_DP[i - 1] * nums[i])
            Min_DP[i] = min(Max_DP[i - 1] * nums[i], nums[i], Min_DP[i - 1] * nums[i])
        return max(Max_DP)
