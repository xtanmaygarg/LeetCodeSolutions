class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 2
        count = 2
        while(j < len(nums)):
            if nums[i - 1] != nums[j]:
                i += 1
                nums[i] = nums[j]
                count += 1
            j += 1
        return count
        
