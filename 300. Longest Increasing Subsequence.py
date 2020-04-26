class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 0:
            return 0
        memo = [1] * L
        for i in range(L - 1):
            for j in range(i + 1, L):
                if nums[i] < nums[j] and (memo[i] + 1) > memo[j]:
                    memo[j] = memo[i] + 1
        return max(memo)
