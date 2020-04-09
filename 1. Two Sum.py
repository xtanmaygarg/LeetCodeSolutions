class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        L = len(nums)
        for i in range(L):
            try:
                if D[target - nums[i]] or D[target - nums[i]] == 0:
                    return [D[target - nums[i]], i]
            except Exception:
                D[nums[i]] = i
