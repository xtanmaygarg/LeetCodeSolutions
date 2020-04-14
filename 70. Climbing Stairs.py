class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        else:
            a = 2
            b = 3
            for i in range(3, n):
                a, b = b, a + b
            return b
