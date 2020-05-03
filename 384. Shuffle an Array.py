class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums        

    def shuffle(self) -> List[int]:
        from random import randrange
        for i in range(len(self.nums)):
            In = randrange(i, len(self.nums))
            self.nums[i], self.nums[In] = self.nums[In], self.nums[i]
        return self.nums
