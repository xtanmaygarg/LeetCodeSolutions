class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            Num = float(s)
            return True
        except Exception:
            return False
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip()
        dot=ee=digit=False
        for i, char in enumerate(s):
            if char in ['+','-']:
                if i>0 and s[i-1]!='e':
                    return False
            elif char=='.':
                if dot or ee: return False
                dot=True
            elif char=='e':
                if ee or not digit: return False
                ee, digit=True, False
            elif char.isdigit():
                digit=True
            else:
                return False
        return digit
"""
