class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        longest = 0
        Set = set(nums)
        
        for num in nums:
            if num - 1 not in Set:
                Current = num
                Streak = 1
                while Current + 1 in Set:
                    Current += 1
                    Streak += 1
                longest = max(longest, Streak)
        return longest
