class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Num = 0
        for i in nums:
            Num = Num ^ i
        return Num
