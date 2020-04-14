class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            out = self.solver(s, i, i)
            if len(out) > len(res):
                res = out
            
            out = self.solver(s, i, i + 1)
            if len(out) > len(res):
                res = out
        
        return res
    
    def solver(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
