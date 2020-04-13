class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 0
        T = 1
        while(i < len(nums)):
            if nums[i] == nums[j]:
                i += 1
            else:
                nums[j + 1] = nums[i]
                j += 1
                T += 1
        return T             
                
