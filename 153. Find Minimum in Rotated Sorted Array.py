class Solution:
    def findMin(self, nums: List[int]) -> int:
        Start = 0
        End = len(nums) - 1
        if nums[0] <= nums[-1]:
            return nums[0]
        while(Start <= End):
            Mid = (Start + End) // 2
            if nums[Mid] > nums[Mid + 1]: 
                return nums[Mid + 1]
            elif nums[Mid] < nums[Mid - 1]:
                return nums[Mid]
            elif nums[Mid] > nums[0]:
                Start = Mid + 1
            else:
                End = Mid - 1
