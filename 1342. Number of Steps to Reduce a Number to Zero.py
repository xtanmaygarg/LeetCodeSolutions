class Solution:
    def numberOfSteps (self, num: int) -> int:
        Answer = -1
        while(num):
            if num & 1:
                Answer += 2
            else:
                Answer += 1
            num = num >> 1
        return Answer
