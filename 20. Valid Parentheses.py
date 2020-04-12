class Solution:
    def isValid(self, s: str) -> bool:
        Len = len(s)
        if Len == 0:
            return True
        Stack = []
        j = 0
        Flag = True
        for i in range(Len):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                Stack.append(s[i])
            else:
                if len(Stack) == 0:
                    Flag = False
                    break
                elif (Stack[-1] + s[i]) in ["[]", "{}", "()"]:
                    Stack.pop()
                else:
                    Flag = False
                    break
            j += 1
        if not Flag or Stack:
            return False
        else:
            return True
