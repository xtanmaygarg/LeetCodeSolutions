class Solution:
    def factorial(m):
        if m < 2:
            return 1
        return m * factorial(m - 1)
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // (factorial(n - 1) * factorial(m - 1))
