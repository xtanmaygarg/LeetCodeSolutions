class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        Stack_S = []
        Stack_T = []
        for i in S:
            if i == '#':
                try:
                    Stack_S.pop()
                except Exception:
                    pass
            else:
                Stack_S.append(i)
        
        for i in T:
            if i == '#':
                try:
                    Stack_T.pop()
                except Exception:
                    pass
            else:
                Stack_T.append(i)
        
        if Stack_S == Stack_T:
            return True
        else:
            return False
        
