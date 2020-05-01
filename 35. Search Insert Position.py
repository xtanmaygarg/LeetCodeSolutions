class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        Left = 0
        Right = len(nums) - 1
        while(Left <= Right):
            Mid = (Left + Right) // 2
            if nums[Mid] == target:
                return Mid
            if nums[Mid] < target:
                if nums[Mid + 1] > target:
                    return Mid + 1
                else:
                    Left = Mid + 1
            else:
                Right = Mid - 1
                
