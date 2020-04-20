class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 0:
            return 0
        if L == 1:
            return nums[0]
        DP = []
        DP.append(nums[0])
        DP.append(max(nums[0], nums[1]))
        for i in range(2, L):
            DP.append(max(nums[i] + DP[i - 2], DP[i - 1]))
        return DP[L - 1]
