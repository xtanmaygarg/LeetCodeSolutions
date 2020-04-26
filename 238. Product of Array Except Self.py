class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        Output = [1] * L
        Curr = 1
        for i in range(1, L):
            Output[i] = Curr * nums[i - 1]
            Curr = Curr * nums[i - 1]
        Curr = 1
        for i in range(L - 2, -1, -1):
            Output[i] = Curr * nums[i + 1] * Output[i]
            Curr = Curr * nums[i + 1]
        return Output
            
